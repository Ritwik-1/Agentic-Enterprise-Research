from langgraph.graph import StateGraph, START, END

from src.state import ReportState
from src.agents import accumulator, research, drafter, validator


def build_graph():
    """Wire the four agents into a LangGraph: Accumulator -> Research -> Drafter -> Validator."""
    graph = StateGraph(ReportState)

    graph.add_node("accumulator", accumulator.run)
    graph.add_node("research", research.run)
    graph.add_node("drafter", drafter.run)
    graph.add_node("validator", validator.run)

    graph.add_edge(START, "accumulator")
    graph.add_edge("accumulator", "research")
    graph.add_edge("research", "drafter")
    graph.add_edge("drafter", "validator")
    graph.add_edge("validator", END)

    return graph.compile()
