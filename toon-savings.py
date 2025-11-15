from toon_format import estimate_savings, compare_formats, count_tokens, encode

# Measure savings
data = {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
result = estimate_savings(data)
print(f"Saves {result['savings_percent']:.1f}% tokens")  # Saves 42.3% tokens

# Visual comparison
print(compare_formats(data))
# Format Comparison
# ────────────────────────────────────────────────
# Format      Tokens    Size (chars)
# JSON            45             123
# TOON            28              85
# ────────────────────────────────────────────────
# Savings: 17 tokens (37.8%)

# Count tokens directly
toon_str = encode(data)
tokens = count_tokens(toon_str)  # Uses tiktoken (gpt5/gpt5-mini)