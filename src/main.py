from src.graph import build_graph


def run_query(query: str) -> str:
    app = build_graph()
    result = app.invoke({"query": query})
    return result["final_report"]


if __name__ == "__main__":
    report = run_query("example query")
    print(report)
