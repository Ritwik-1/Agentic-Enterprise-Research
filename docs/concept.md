# Enterprise Research Agent — Concept

## Agents

- **Accumulator** — pulls relevant info from the company's internal knowledge base.
- **Research** — searches the internet for relevant market info.
- **Drafter** — combines Accumulator + Research output into a professional document.
- **Validator** — checks the drafted document for accuracy/consistency before it's final.

## Tools (starter set)

- Web search (for Research agent)
- Knowledge base retrieval (for Accumulator agent) — V2 only
- Document formatter (for Drafter agent)

## State (shared across agents)

```
query: str
kb_context: str        # from Accumulator
market_research: str   # from Research
draft: str              # from Drafter
validation_notes: str   # from Validator
final_report: str
```

## Diagram

```
User Query
    |
    v
Accumulator Agent  (KB lookup — empty/no-op in V1)
    |
    v
Research Agent  (internet search)
    |
    v
Drafter Agent  (writes the report using kb_context + market_research)
    |
    v
Validator Agent  (checks the draft)
    |
    v
Final Report -> UI
```

## V1 vs V2

- **V1**: No knowledge base. Accumulator agent exists but is a no-op/empty (returns nothing). Goal is a *functional UI* that takes a user query and returns a report, using only internet research (Research -> Drafter -> Validator).
- **V2**: Accumulator agent becomes real — connects to the company knowledge base and feeds relevant internal context into the Drafter alongside market research.

## Eval metrics

- **Faithfulness / groundedness** — does every claim in the final report trace back to a retrieved source (web result or KB chunk)? Core RAGAS-style metric, main defense against hallucination.
- **Context precision / recall** — of what Research (and later Accumulator) retrieved, how much was actually relevant and used, and how much relevant info was missed.
- **Answer relevance** — does the final report actually address the user's query, not just a tangential topic.
- **Citation accuracy** — do cited sources actually say what's attributed to them (sampled/LLM-judged).
- **Critic/Validator catch rate** — % of injected or known errors the Validator agent actually flags before final output (measures whether validation is doing real work, not rubber-stamping).
- **Task completion rate** — % of queries that produce a final report at all vs. erroring out or stalling.
- **Agent trajectory efficiency** — tool calls / agent hops per run; flags loops or redundant research passes.
- **Latency & cost per report** — wall-clock time and token spend end-to-end; tracked per agent to find the bottleneck.
- **LLM-as-judge pairwise preference** — periodically compare report versions (model/prompt changes) head-to-head instead of relying on a single absolute score.
