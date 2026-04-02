"""
Chapter 2: The Transformer Architecture
- Scaled dot-product attention
- Multi-head attention
- Positional encoding
- Attention visualization
"""

# %% 1. Scaled dot-product attention from scratch
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V, mask=None):
    """Compute scaled dot-product attention."""
    d_k = Q.size(-1)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, V), weights

Q = torch.randn(1, 4, 8)
K = torch.randn(1, 4, 8)
V = torch.randn(1, 4, 8)
output, attn_weights = scaled_dot_product_attention(Q, K, V)
print(f"Output shape: {output.shape}")
print(f"Attention weights shape: {attn_weights.shape}")
print(f"Attention weights (row sums): {attn_weights.sum(dim=-1)}")

# %% 2. Multi-head attention
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=512, num_heads=8):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_k = d_model // num_heads
        self.num_heads = num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, Q, K, V, mask=None):
        batch = Q.size(0)
        Q = self.W_q(Q).view(batch, -1, self.num_heads, self.d_k).transpose(1, 2)
        K = self.W_k(K).view(batch, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = self.W_v(V).view(batch, -1, self.num_heads, self.d_k).transpose(1, 2)
        out, weights = scaled_dot_product_attention(Q, K, V, mask)
        out = out.transpose(1, 2).contiguous().view(batch, -1, self.num_heads * self.d_k)
        return self.W_o(out)

mha = MultiHeadAttention(d_model=64, num_heads=4)
x = torch.randn(2, 10, 64)
print(f"\nMulti-head attention output: {mha(x, x, x).shape}")

# %% 3. Positional encoding
import numpy as np
import matplotlib.pyplot as plt

def positional_encoding(max_len, d_model):
    pe = np.zeros((max_len, d_model))
    position = np.arange(max_len)[:, np.newaxis]
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
    pe[:, 0::2] = np.sin(position * div_term)
    pe[:, 1::2] = np.cos(position * div_term)
    return pe

pe = positional_encoding(100, 64)
plt.figure(figsize=(10, 4))
plt.imshow(pe, aspect="auto", cmap="RdBu")
plt.xlabel("Embedding dimension")
plt.ylabel("Position")
plt.title("Sinusoidal positional encoding")
plt.colorbar()
plt.tight_layout()
plt.savefig("positional_encoding.png", dpi=150)
plt.show()
print("Saved positional_encoding.png")

# %% 4. Attention visualization with DistilBERT
from transformers import AutoTokenizer, AutoModel
import seaborn as sns

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, output_attentions=True)

text = "The cat sat on the mat because it was tired"
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

attn = outputs.attentions[-1][0]  # last layer, first batch
tokens_list = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

fig, axes = plt.subplots(1, 4, figsize=(20, 5))
for i, ax in enumerate(axes):
    sns.heatmap(attn[i].numpy(), xticklabels=tokens_list,
                yticklabels=tokens_list, ax=ax, cmap="Blues")
    ax.set_title(f"Head {i}")
plt.tight_layout()
plt.savefig("attention_heads.png", dpi=150)
plt.show()
print("Saved attention_heads.png")

# %% 5. Parameter counting
def count_transformer_params(d_model, num_heads, d_ff=None):
    """Count parameters in one Transformer encoder layer."""
    if d_ff is None:
        d_ff = 4 * d_model
    # Multi-head attention: 4 linear layers (Q, K, V, O)
    mha_params = 4 * (d_model * d_model + d_model)
    # Feed-forward: 2 linear layers
    ff_params = d_model * d_ff + d_ff + d_ff * d_model + d_model
    # Layer norms: 2 * (2 * d_model)
    ln_params = 2 * (2 * d_model)
    total = mha_params + ff_params + ln_params
    print(f"\nd_model={d_model}, heads={num_heads}, d_ff={d_ff}")
    print(f"  MHA params:   {mha_params:>10,}")
    print(f"  FF params:    {ff_params:>10,}")
    print(f"  LayerNorm:    {ln_params:>10,}")
    print(f"  Total/layer:  {total:>10,}")
    return total

count_transformer_params(512, 8)
count_transformer_params(768, 12)  # BERT-base
