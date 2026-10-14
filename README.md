# Enterprise Research Agent

Multi-agent system that takes a user query and produces a professional research report, combining internal company knowledge with live internet research.

## Agents

| Agent | Role |
|---|---|
| Accumulator | Pulls relevant context from the company knowledge base (V2; no-op in V1) |
| Research | Searches the internet for relevant market info |
| Drafter | Drafts a professional document from the above |
| Validator | Checks the draft for accuracy/consistency before it's final |

See [docs/concept.md](docs/concept.md) for the full design (state, diagram, eval metrics) and [`tech-stack.md`](../tech-stack.md) for the stack.

## Status

**V1** — no knowledge base yet. Goal is a functional UI that returns a report for any query, using internet research only.

## Project structure

```
src/
  state.py        # shared state passed between agents
  agents/          # accumulator, research, drafter, validator
  tools/           # web_search, etc.
  graph.py        # LangGraph wiring
  main.py          # entrypoint
```

## Setup

```bash
python -m venv EraEnv
source EraEnv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in API keys
```

## Run

```bash
python -m src.main
```
