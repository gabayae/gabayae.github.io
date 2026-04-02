"""
Chapter 9: LLM Agents and Tool Use
- ReAct pattern
- Function calling with Groq
- LangChain agents
- Multi-step reasoning
- LangGraph workflows
"""

import os
import json
# os.environ["GROQ_API_KEY"] = "your-key"
# os.environ["GOOGLE_API_KEY"] = "your-key"

# %% 1. Function calling with Groq
from groq import Groq

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"},
                },
                "required": ["expression"],
            },
        },
    },
]

def get_weather(city, unit="celsius"):
    return {"city": city, "temperature": 28, "unit": unit, "condition": "sunny"}

def calculate(expression):
    return {"result": eval(expression)}

tool_map = {"get_weather": get_weather, "calculate": calculate}

# Agent loop
messages = [{"role": "user", "content": "What is the temperature in Cotonou?"}]

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

msg = response.choices[0].message
if msg.tool_calls:
    messages.append(msg)
    for tc in msg.tool_calls:
        func_name = tc.function.name
        args = json.loads(tc.function.arguments)
        result = tool_map[func_name](**args)
        messages.append({
            "role": "tool",
            "tool_call_id": tc.id,
            "content": json.dumps(result),
        })
    final = client.chat.completions.create(
        model="llama-3.1-8b-instant", messages=messages
    )
    print("Function calling result:")
    print(final.choices[0].message.content)
else:
    print(msg.content)

# %% 2. LangChain agent with tools
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

@tool
def search_arxiv(query: str) -> str:
    """Search arxiv.org for recent papers. Returns titles and abstracts."""
    import urllib.request
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results=3"
    response = urllib.request.urlopen(url).read().decode()
    return response[:2000]

@tool
def python_calculator(expression: str) -> str:
    """Evaluate a Python math expression. Example: '2**10 + 3*4'"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
tools_list = [search_arxiv, python_calculator]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful research assistant. Use tools when needed."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools_list, prompt)
executor = AgentExecutor(agent=agent, tools=tools_list, verbose=True)

print("\nLangChain agent:")
result = executor.invoke({"input": "What is 2^20 + 3^10?"})
print(result["output"])

# %% 3. LangGraph multi-step workflow
from langgraph.graph import StateGraph, END
from typing import TypedDict

class AgentState(TypedDict):
    question: str
    research: str
    draft: str
    review: str
    final_answer: str

def research_step(state: AgentState) -> AgentState:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    result = llm.invoke(f"Research this topic thoroughly: {state['question']}")
    return {"research": result.content}

def draft_step(state: AgentState) -> AgentState:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    result = llm.invoke(
        f"Based on this research:\n{state['research']}\n\n"
        f"Write a clear, concise answer to: {state['question']}"
    )
    return {"draft": result.content}

def review_step(state: AgentState) -> AgentState:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    result = llm.invoke(
        f"Review this draft for accuracy and clarity:\n{state['draft']}"
    )
    return {"review": result.content}

def finalize_step(state: AgentState) -> AgentState:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    result = llm.invoke(
        f"Original draft:\n{state['draft']}\n\nReview feedback:\n{state['review']}\n\n"
        f"Write the final polished answer."
    )
    return {"final_answer": result.content}

workflow = StateGraph(AgentState)
workflow.add_node("research", research_step)
workflow.add_node("draft", draft_step)
workflow.add_node("review", review_step)
workflow.add_node("finalize", finalize_step)

workflow.set_entry_point("research")
workflow.add_edge("research", "draft")
workflow.add_edge("draft", "review")
workflow.add_edge("review", "finalize")
workflow.add_edge("finalize", END)

app = workflow.compile()

print("\nLangGraph workflow:")
result = app.invoke({"question": "What are the key differences between LoRA and QLoRA?"})
print(result["final_answer"])
