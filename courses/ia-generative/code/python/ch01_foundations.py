"""
Chapter 1: Foundations of Language Models
- Tokenization (BPE, WordPiece)
- Embeddings
- Softmax
- Perplexity
- First text generation
"""

# %% 1. Tokenization with tiktoken (GPT tokenizer)
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer
text = "Generative AI transforms how we create content."
tokens = enc.encode(text)
print(f"Text: {text}")
print(f"Token IDs: {tokens}")
print(f"Tokens: {[enc.decode([t]) for t in tokens]}")
print(f"Number of tokens: {len(tokens)}")

# %% 2. Compare BPE (GPT-2) and WordPiece (BERT) tokenizers
from transformers import AutoTokenizer

gpt2_tok = AutoTokenizer.from_pretrained("gpt2")
bert_tok = AutoTokenizer.from_pretrained("distilbert-base-uncased")

sentence = "Pneumonoultramicroscopicsilicovolcanoconiosis is a lung disease."
print(f"\nGPT-2 tokens: {gpt2_tok.tokenize(sentence)}")
print(f"BERT tokens:  {bert_tok.tokenize(sentence)}")
print(f"GPT-2 count:  {len(gpt2_tok.tokenize(sentence))}")
print(f"BERT count:   {len(bert_tok.tokenize(sentence))}")

# %% 3. Embeddings with DistilBERT
import torch
from transformers import AutoModel

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

text = "The patient has a fever."
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

print(f"\nEmbedding shape: {outputs.last_hidden_state.shape}")
print(f"Embedding dim: {outputs.last_hidden_state.shape[-1]}")

# %% 4. Softmax function
import torch.nn.functional as F

logits = torch.tensor([2.0, 1.0, 0.5, -1.0, 3.0])
probs = F.softmax(logits, dim=0)
print(f"\nLogits: {logits.tolist()}")
print(f"Probabilities: {[f'{p:.4f}' for p in probs.tolist()]}")
print(f"Sum: {probs.sum().item():.4f}")

# %% 5. Perplexity
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model.eval()

texts = [
    "The Transformer architecture revolutionized natural language processing.",
    "Processing language natural revolutionized architecture Transformer the.",
    "Le chat est sur le tapis.",
]

for text in texts:
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
        ppl = torch.exp(outputs.loss).item()
    print(f"PPL={ppl:>8.2f} | {text}")

# %% 6. First text generation
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
result = generator(
    "Artificial intelligence will",
    max_new_tokens=50,
    do_sample=True,
    temperature=0.8,
)
print(f"\nGenerated text:\n{result[0]['generated_text']}")
