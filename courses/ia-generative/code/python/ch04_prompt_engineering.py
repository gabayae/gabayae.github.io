"""
Chapter 4: Prompt Engineering
- Zero-shot, few-shot, chain-of-thought
- Role prompting
- Structured output (JSON)
- Prompt templates
"""

import os
# Set API keys before running
# os.environ["GROQ_API_KEY"] = "your-key"
# os.environ["GOOGLE_API_KEY"] = "your-key"

# %% 1. Helper functions for Groq and Gemini
from groq import Groq

client = Groq()

def ask_groq(prompt, model="llama-3.1-8b-instant", temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=1024,
    )
    return response.choices[0].message.content

import google.generativeai as genai
genai.configure()
gemini = genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(prompt, temperature=0.7):
    response = gemini.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(temperature=temperature),
    )
    return response.text

# %% 2. Zero-shot classification
prompt = """Classify the following movie review as POSITIVE or NEGATIVE.

Review: "The cinematography was breathtaking, but the plot was
completely incoherent and the acting felt wooden."

Classification:"""

print("Zero-shot classification:")
print(ask_groq(prompt, temperature=0))

# %% 3. Few-shot translation
prompt = """Translate English to French.

English: The weather is beautiful today.
French: Le temps est magnifique aujourd'hui.

English: I would like a cup of coffee, please.
French: Je voudrais une tasse de cafe, s'il vous plait.

English: Where is the nearest hospital?
French:"""

print("\nFew-shot translation:")
print(ask_groq(prompt, temperature=0.2))

# %% 4. Chain-of-thought prompting
prompt_direct = "If a train travels 120 km in 1.5 hours, and then 80 km in 1 hour, what is the average speed for the entire trip?"

prompt_cot = """If a train travels 120 km in 1.5 hours, and then 80 km in 1 hour, what is the average speed for the entire trip?

Let's think step by step:"""

print("\n=== Direct ===")
print(ask_groq(prompt_direct, temperature=0))
print("\n=== Chain-of-Thought ===")
print(ask_groq(prompt_cot, temperature=0))

# %% 5. Role prompting with system message
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": (
            "You are an expert data scientist. You explain concepts "
            "clearly using analogies. You always provide Python code "
            "examples. You never use jargon without defining it first."
        )},
        {"role": "user", "content": "Explain overfitting to a beginner."},
    ],
    temperature=0.7,
)
print("\nRole prompting:")
print(response.choices[0].message.content)

# %% 6. Structured output (JSON)
import json

prompt = """Extract the following information from the text and return
it as a JSON object with keys: name, age, condition, medication.

Text: "Mrs. Fatou Diallo, 67 years old, was diagnosed with
Type 2 diabetes last year. She takes Metformin 500mg twice daily."

JSON:"""

result = ask_groq(prompt, temperature=0)
print("\nStructured output:")
print(result)
try:
    data = json.loads(result)
    print(f"Patient: {data['name']}, Age: {data['age']}")
except json.JSONDecodeError:
    print("Note: JSON parsing failed, model output needs cleanup")

# %% 7. Prompt templates
from string import Template

summarizer = Template("""Summarize the following $doc_type in $num_sentences sentences.
Focus on: $focus_area

Text:
$text

Summary:""")

prompt = summarizer.substitute(
    doc_type="research paper abstract",
    num_sentences="3",
    focus_area="methodology and key findings",
    text="We propose LoRA, a method for adapting large language models by training low-rank decomposition matrices instead of all model parameters. LoRA reduces the number of trainable parameters by 10,000x and GPU memory by 3x compared to full fine-tuning, with no loss in quality."
)
print("\nPrompt template result:")
print(ask_groq(prompt))

# %% 8. LangChain prompt template
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. Respond in {language}."),
    ("human", "{question}"),
])

prompt = template.invoke({
    "role": "medical doctor",
    "language": "French",
    "question": "What are the symptoms of malaria?",
})
print("\nLangChain template:")
print(prompt.to_string())
