"""
Chapter 10: Capstone Projects
- Project 1: RAG on PDF corpus
- Project 2: Domain chatbot fine-tuning (dataset creation)
- Project 3: Image generation pipeline
- Project 4: Multi-agent research assistant
- Project 5: LLM evaluation benchmark
"""

# %% Project 1: RAG with source tracking
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def build_rag_app(pdf_dir="./pdf_corpus/"):
    """Build a RAG application over a PDF directory."""
    loader = PyPDFDirectoryLoader(pdf_dir)
    docs = loader.load()
    print(f"Loaded {len(docs)} pages")

    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=80)
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)

    template = ChatPromptTemplate.from_template(
        """Answer the question based on the context. Include source references.

Context:
{context}

Question: {question}

Answer (with sources):"""
    )

    def format_docs_with_sources(docs):
        return "\n\n".join(
            f"[{d.metadata.get('source','?')}, p.{d.metadata.get('page','?')}]\n{d.page_content}"
            for d in docs
        )

    chain = (
        {"context": retriever | format_docs_with_sources,
         "question": RunnablePassthrough()}
        | template | llm | StrOutputParser()
    )
    return chain

# Usage: chain = build_rag_app("./my_pdfs/")
# answer = chain.invoke("What is the main finding?")

# %% Project 2: Dataset creation for fine-tuning
import json

def create_instruction_dataset(topic, num_examples=50):
    """Generate instruction-response pairs using an LLM."""
    from groq import Groq
    client = Groq()

    prompt = f"""Generate {num_examples} diverse instruction-response pairs
about {topic}. Format as a JSON array with keys: instruction, response.
Each response should be 2-4 sentences. Be accurate and educational."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=4096,
    )

    try:
        pairs = json.loads(response.choices[0].message.content)
        return pairs
    except json.JSONDecodeError:
        print("JSON parsing failed. Raw output:")
        print(response.choices[0].message.content[:500])
        return []

# pairs = create_instruction_dataset("West African cuisine", 50)
# with open("cooking_dataset.json", "w") as f:
#     json.dump(pairs, f, indent=2)

# %% Project 3: Image generation with style presets
from diffusers import StableDiffusionPipeline
import torch

class ImageGenerator:
    STYLE_PROMPTS = {
        "photorealistic": "photorealistic, 8k, highly detailed, sharp focus",
        "watercolor": "watercolor painting, soft colors, artistic",
        "digital_art": "digital art, vibrant colors, detailed illustration",
        "sketch": "pencil sketch, black and white, detailed drawing",
        "oil_painting": "oil painting, rich textures, masterpiece",
    }

    def __init__(self, model_id="stabilityai/stable-diffusion-2-1-base"):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id, torch_dtype=torch.float16
        ).to("cuda")

    def generate(self, prompt, style="photorealistic", seed=42, **kwargs):
        styled_prompt = f"{prompt}, {self.STYLE_PROMPTS[style]}"
        generator = torch.Generator("cuda").manual_seed(seed)
        return self.pipe(
            styled_prompt,
            negative_prompt="blurry, low quality, deformed",
            generator=generator,
            num_inference_steps=30,
            guidance_scale=7.5,
            **kwargs,
        ).images[0]

# gen = ImageGenerator()
# for style in ImageGenerator.STYLE_PROMPTS:
#     img = gen.generate("A bustling market in Cotonou", style=style)
#     img.save(f"market_{style}.png")

# %% Project 4: Multi-agent research assistant
from langgraph.graph import StateGraph, END
from typing import TypedDict

class ResearchState(TypedDict):
    topic: str
    research_notes: str
    draft: str
    review: str
    revision_count: int
    final_report: str

def build_research_assistant():
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)

    def researcher(state):
        result = llm.invoke(f"Research: {state['topic']}. Include facts and stats.")
        return {"research_notes": result.content}

    def writer(state):
        feedback = f"\nPrevious review: {state.get('review', '')}" if state.get("review") else ""
        result = llm.invoke(f"Write a report based on:\n{state['research_notes']}{feedback}")
        return {"draft": result.content, "revision_count": state.get("revision_count", 0) + 1}

    def reviewer(state):
        result = llm.invoke(f"Review for accuracy and clarity:\n{state['draft']}\nSay APPROVED if good.")
        return {"review": result.content}

    def should_revise(state):
        if state.get("revision_count", 0) >= 3 or "APPROVED" in state.get("review", ""):
            return "finalize"
        return "revise"

    def finalize(state):
        return {"final_report": state["draft"]}

    workflow = StateGraph(ResearchState)
    workflow.add_node("research", researcher)
    workflow.add_node("write", writer)
    workflow.add_node("review", reviewer)
    workflow.add_node("finalize", finalize)
    workflow.set_entry_point("research")
    workflow.add_edge("research", "write")
    workflow.add_edge("write", "review")
    workflow.add_conditional_edges("review", should_revise, {"revise": "write", "finalize": "finalize"})
    workflow.add_edge("finalize", END)
    return workflow.compile()

# app = build_research_assistant()
# result = app.invoke({"topic": "AI in African education", "revision_count": 0})
# print(result["final_report"])

# %% Project 5: LLM evaluation benchmark
from rouge_score import rouge_scorer
import numpy as np

class LLMBenchmark:
    def __init__(self):
        self.scorer = rouge_scorer.RougeScorer(
            ["rouge1", "rouge2", "rougeL"], use_stemmer=True
        )
        self.results = []

    def add_test_case(self, category, question, reference_answer):
        self.results.append({
            "category": category,
            "question": question,
            "reference": reference_answer,
            "model_outputs": {},
        })

    def evaluate_model(self, model_name, generate_fn):
        for case in self.results:
            output = generate_fn(case["question"])
            scores = self.scorer.score(case["reference"], output)
            case["model_outputs"][model_name] = {
                "output": output,
                "rouge1_f1": scores["rouge1"].fmeasure,
                "rouge2_f1": scores["rouge2"].fmeasure,
                "rougeL_f1": scores["rougeL"].fmeasure,
            }

    def summary(self):
        if not self.results or not self.results[0]["model_outputs"]:
            print("No results yet.")
            return
        for model in self.results[0]["model_outputs"]:
            r1 = np.mean([c["model_outputs"][model]["rouge1_f1"] for c in self.results])
            r2 = np.mean([c["model_outputs"][model]["rouge2_f1"] for c in self.results])
            rl = np.mean([c["model_outputs"][model]["rougeL_f1"] for c in self.results])
            print(f"{model}: ROUGE-1={r1:.3f}, ROUGE-2={r2:.3f}, ROUGE-L={rl:.3f}")

# Demo
bench = LLMBenchmark()
bench.add_test_case("factual", "What is the capital of Benin?",
                    "The capital of Benin is Porto-Novo.")
bench.add_test_case("reasoning", "If A > B and B > C, is A > C?",
                    "Yes, by transitivity, A > C.")
bench.add_test_case("summarization", "Summarize: LoRA trains low-rank adapters.",
                    "LoRA is an efficient fine-tuning method using low-rank matrices.")
print("Benchmark created with", len(bench.results), "test cases.")
print("Use bench.evaluate_model('model_name', generate_fn) to evaluate.")
