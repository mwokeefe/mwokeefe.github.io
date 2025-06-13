title: Precise length control for large language models
date: 01/01/2020

# Introduction
Controlling output length in large language models (LLMs) is a persistent challenge, especially in production systems where structured responses or consistent verbosity are essential. Standard prompting techniques and maximum token limits offer only coarse control, often resulting in outputs that are too short, too long, or unnaturally truncated.

To address this, we introduce a simple but effective method to enable precise response length control in decoder-only transformer architectures using Length-Difference Positional Encoding (LDPE).

# The Core Idea: Countdown Positional Encoding

LDPE works by injecting an additional positional signal into the model that counts down from a user-defined target response length. Instead of altering the model's existing RoPE or absolute positional encodings — which would likely degrade performance — we add a secondary sinusoidal encoding to the input token embeddings. This reverse positional signal indicates how many tokens remain until the response should terminate.

Two variations were tested:

LDPE: Applies the countdown across the full prompt-response sequence.
ORPE: Offsets the countdown to begin only at the start of the generated response.
We fine-tune open-weight LLMs (e.g., Mistral 7B, LLaMA 3 8B) with this additional countdown signal. During training, the model learns to interpret the countdown as a form of token budget, allowing it to structure responses to end cleanly when the countdown reaches zero.

# Integration and Training

The reverse encodings are constructed using the standard sinusoidal formula and added directly to the token embeddings. To avoid scale mismatches between the learned embeddings and the sinusoidal signals, we normalize the added encoding using Frobenius norm scaling.

Fine-tuning is performed using LoRA adapters, allowing efficient adaptation without overwriting pretrained weights. We found that a single epoch on a modest-sized dataset (~110k QA samples from OpenOrca and MMLU) was sufficient to achieve strong length control.

# Results: Sub-Token Accuracy Without Quality Loss

On a QA benchmark with variable-length targets (10–200 tokens), LDPE-fine-tuned models consistently generated outputs within 2–3 tokens of the target length. This level of control was an order of magnitude more accurate than prompt-only fine-tuning approaches.

We also tested summarization on CNN/DailyMail using GPT-3.5-generated summaries as soft references. Summary quality, as measured by BERT and ROUGE scores, was on par with prompt-based baselines, but LDPE models matched the target length 10x more accurately.

To ensure the model’s general capabilities weren’t compromised, we evaluated it on several standard NLP benchmarks (ARC, PIQA, HellaSwag, WINOGRANDE). Task performance was largely preserved after fine-tuning, with no major regressions except a small drop on HellaSwag.

# Takeaways

LDPE enables fine-grained, token-level control over LLM output length with minimal overhead:

No changes to model architecture
Compatible with any decoder-only LLM
Maintains performance across QA, summarization, and benchmark tasks
Enables smoother response termination and better format compliance
This approach unlocks new capabilities for LLM deployments where deterministic length behavior is critical — including multi-step reasoning chains, format-sensitive APIs, and human-in-the-loop systems.

# Citing articles
Add...