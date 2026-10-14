from typing import TypedDict


class ReportState(TypedDict):
    query: str
    kb_context: str
    market_research: str
    draft: str
    validation_notes: str
    final_report: str
