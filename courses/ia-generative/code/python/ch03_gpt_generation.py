"""
Chapter 3: GPT and Text Generation
- Autoregressive generation loop
- Decoding strategies (greedy, temperature, top-k, top-p, beam search)
- HuggingFace generate() API
- Repetition control
"""

# %% 1. Manual autoregressive generation
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

prompt = "The future of artificial intelligence"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

generated = input_ids.clone()
for _ in range(30):
    with torch.no_grad():
        outputs = model(generated)
        next_logits = outputs.logits[:, -1, :]
        next_token = torch.argmax(next_logits, dim=-1, keepdim=True)
        generated = torch.cat([generated, next_token], dim=-1)

print("Manual greedy generation:")
print(tokenizer.decode(generated[0]))

# %% 2. Top-k sampling from scratch
import torch.nn.functional as F

def top_k_sample(logits, k=10, temperature=1.0):
    """Sample from the top-k logits with temperature."""
    scaled = logits / temperature
    top_k_vals, top_k_idx = torch.topk(scaled, k)
    probs = F.softmax(top_k_vals, dim=-1)
    sampled_idx = torch.multinomial(probs, 1)
    return top_k_idx.gather(-1, sampled_idx)

# Test
logits = torch.randn(1, 50257)  # GPT-2 vocab size
token = top_k_sample(logits, k=10, temperature=0.8)
print(f"\nSampled token ID: {token.item()}")

# %% 3. All decoding strategies with pipeline
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "In 2026, the most important AI breakthrough was"

strategies = {
    "Greedy": {"do_sample": False},
    "Temp 0.3": {"do_sample": True, "temperature": 0.3},
    "Temp 1.5": {"do_sample": True, "temperature": 1.5},
    "Top-k 10": {"do_sample": True, "top_k": 10},
    "Top-p 0.9": {"do_sample": True, "top_p": 0.9},
    "Beam 4": {"do_sample": False, "num_beams": 4},
}

for name, params in strategies.items():
    result = generator(prompt, max_new_tokens=50, **params)
    print(f"\n=== {name} ===")
    print(result[0]["generated_text"])

# %% 4. TinyLlama chat generation
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype="auto", device_map="auto"
)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Explain gradient descent in 3 sentences."},
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False,
                                        add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

output = model.generate(
    **inputs, max_new_tokens=150, temperature=0.7,
    top_p=0.9, do_sample=True, repetition_penalty=1.1,
)
print("\nTinyLlama response:")
print(tokenizer.decode(output[0], skip_special_tokens=True))

# %% 5. Repetition control
print("\n=== Without repetition penalty ===")
out1 = generator("Once upon a time", max_new_tokens=80, do_sample=True,
                  temperature=0.8)
print(out1[0]["generated_text"])

print("\n=== With repetition penalty 1.2 ===")
out2 = generator("Once upon a time", max_new_tokens=80, do_sample=True,
                  temperature=0.8, repetition_penalty=1.2)
print(out2[0]["generated_text"])

# %% 6. Generation speed measurement
import time

def measure_speed(model, tokenizer, prompt, n_tokens=100):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    start = time.time()
    output = model.generate(**inputs, max_new_tokens=n_tokens, do_sample=False)
    elapsed = time.time() - start
    generated_tokens = output.shape[1] - inputs["input_ids"].shape[1]
    speed = generated_tokens / elapsed
    print(f"Generated {generated_tokens} tokens in {elapsed:.2f}s ({speed:.1f} tok/s)")

model_gpt2 = GPT2LMHeadModel.from_pretrained("gpt2")
tok_gpt2 = GPT2Tokenizer.from_pretrained("gpt2")
measure_speed(model_gpt2, tok_gpt2, "The meaning of life is")
