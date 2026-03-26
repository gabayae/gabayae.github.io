"""
Chapter 6: Attention Mechanism
Scaled dot-product and multi-head attention from scratch
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class ScaledDotProductAttention(nn.Module):
    """Scaled dot-product attention."""
    def forward(self, Q, K, V, mask=None):
        d_k = Q.size(-1)
        scores = Q @ K.transpose(-2, -1) / math.sqrt(d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        attn_weights = F.softmax(scores, dim=-1)
        return attn_weights @ V, attn_weights


class MultiHeadAttention(nn.Module):
    """Multi-head attention from scratch."""
    def __init__(self, d_model, n_heads):
        super().__init__()
        assert d_model % n_heads == 0
        self.d_k = d_model // n_heads
        self.n_heads = n_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
        self.attention = ScaledDotProductAttention()

    def forward(self, Q, K, V, mask=None):
        B, L, _ = Q.size()
        # Project and reshape: (B, L, d_model) -> (B, n_heads, L, d_k)
        Q = self.W_q(Q).view(B, L, self.n_heads, self.d_k).transpose(1, 2)
        K = self.W_k(K).view(B, -1, self.n_heads, self.d_k).transpose(1, 2)
        V = self.W_v(V).view(B, -1, self.n_heads, self.d_k).transpose(1, 2)

        out, attn = self.attention(Q, K, V, mask)
        # Concatenate heads
        out = out.transpose(1, 2).contiguous().view(B, L, -1)
        return self.W_o(out), attn


if __name__ == '__main__':
    torch.manual_seed(42)

    B, L, d_model, n_heads = 2, 10, 64, 8
    x = torch.randn(B, L, d_model)

    # Self-attention
    mha = MultiHeadAttention(d_model, n_heads)
    out, attn = mha(x, x, x)
    print(f"Input shape:    {x.shape}")
    print(f"Output shape:   {out.shape}")
    print(f"Attn shape:     {attn.shape}")
    print(f"Attn sum (row): {attn[0, 0, 0].sum().item():.4f} (should be 1)")

    # Causal mask
    causal_mask = torch.tril(torch.ones(L, L)).unsqueeze(0).unsqueeze(0)
    out_causal, attn_causal = mha(x, x, x, mask=causal_mask)
    print(f"\nCausal attn[0,0,0,:5]: {attn_causal[0,0,0,:5].tolist()}")
    print(f"Causal attn[0,0,0,5:]: {attn_causal[0,0,0,5:].tolist()}")
