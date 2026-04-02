"""
Chapter 6: Retrieval-Augmented Generation (RAG)
- Sentence embeddings
- ChromaDB vector store
- FAISS vector search
- Document chunking
- LangChain RAG pipeline
"""

# %% 1. Sentence embeddings and similarity
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The patient has a high fever and cough.",
    "Machine learning is a subset of artificial intelligence.",
    "The patient presents with elevated temperature and respiratory symptoms.",
]

embeddings = model.encode(sentences)
print(f"Embedding shape: {embeddings.shape}")

sim_matrix = cosine_similarity(embeddings)
print("\nSimilarity matrix:")
for i, s in enumerate(sentences):
    print(f"  [{i}] {s[:50]}...")
print(np.round(sim_matrix, 3))

# %% 2. ChromaDB vector store
import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()  # in-memory for demo

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="course_notes", embedding_function=ef
)

documents = [
    "The Transformer architecture uses self-attention mechanisms.",
    "LoRA reduces fine-tuning costs by training low-rank adapters.",
    "RAG retrieves relevant documents before generating answers.",
    "Diffusion models generate images by reversing a noise process.",
    "RLHF aligns language models with human preferences.",
]

collection.add(
    documents=documents,
    ids=[f"doc_{i}" for i in range(len(documents))],
    metadatas=[{"chapter": i + 1} for i in range(len(documents))],
)

results = collection.query(query_texts=["How does fine-tuning work?"], n_results=2)
print("\nChromaDB query results:")
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"  [{dist:.4f}] {doc}")

# %% 3. FAISS vector search
import faiss

documents_faiss = [
    "Python is a high-level programming language.",
    "PyTorch is a deep learning framework.",
    "LangChain helps build LLM applications.",
    "ChromaDB stores vector embeddings.",
    "Transformers use attention mechanisms.",
]

embeddings_faiss = model.encode(documents_faiss).astype("float32")
dimension = embeddings_faiss.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings_faiss)
print(f"\nFAISS index contains {index.ntotal} vectors")

query = model.encode(["How do I build an LLM app?"]).astype("float32")
distances, indices = index.search(query, k=2)
print("FAISS query results:")
for idx, dist in zip(indices[0], distances[0]):
    print(f"  [{dist:.4f}] {documents_faiss[idx]}")

# %% 4. Document chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter

long_text = """
Retrieval-Augmented Generation (RAG) is a technique that enhances
large language models by providing them with relevant external knowledge
at inference time. Instead of relying solely on the information encoded
in model parameters during pre-training, RAG systems first retrieve
relevant documents from a knowledge base, then include those documents
in the prompt to the language model.

The key components of a RAG system are: (1) a document store containing
the knowledge base, (2) an embedding model that converts text to vectors,
(3) a vector database for efficient similarity search, (4) a retrieval
strategy that selects the most relevant documents, and (5) a language
model that generates answers based on the retrieved context.

RAG is particularly useful for applications that require up-to-date
information, domain-specific knowledge, or verifiable answers with
source citations.
""".strip()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""],
)
chunks = splitter.split_text(long_text)
print(f"\nNumber of chunks: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i} ({len(chunk)} chars):\n{chunk[:100]}...")

# %% 5. Complete RAG chain with LangChain
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import Document

# Create documents
docs = [Document(page_content=c, metadata={"chunk": i}) for i, c in enumerate(chunks)]

embeddings_lc = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(docs, embeddings_lc)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)

template = ChatPromptTemplate.from_template(
    """Answer the question based only on the following context.
If you cannot answer from the context, say "I don't have enough information."

Context:
{context}

Question: {question}

Answer:"""
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | template | llm | StrOutputParser()
)

answer = rag_chain.invoke("What are the key components of a RAG system?")
print(f"\nRAG answer:\n{answer}")
