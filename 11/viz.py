from collections import defaultdict
from graphviz import Digraph

def read_graph(path):
    adj = defaultdict(list)
    nodes = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fr, to = line.split(":")
            fr = fr.strip()
            nodes.add(fr)
            for t in to.strip().split():
                nodes.add(t)
                adj[fr].append(t)
    return adj, nodes

def render_graph(adj, nodes, out_file="graph.svg", engine="sfdp",
                 highlight=None, rankdir="LR", max_label_len=40):
    if highlight is None:
        highlight = {}

    dot = Digraph("G", engine=engine)
    dot.attr(
        "graph",
        rankdir=rankdir,
        overlap="false",
        splines="true",
        bgcolor="white"
    )
    dot.attr("node", shape="box", style="rounded,filled", fillcolor="white", color="gray40", fontname="Helvetica")
    dot.attr("edge", color="gray50", arrowsize="0.7")

    # nodes
    for n in sorted(nodes):
        label = n if len(n) <= max_label_len else (n[:max_label_len-1] + "…")
        if n in highlight:
            dot.node(n, label=label, fillcolor=highlight[n], color="gray20")
        else:
            dot.node(n, label=label)

    # edges
    for u, vs in adj.items():
        for v in vs:
            dot.edge(u, v)

    # graphviz python will add the extension; we want exact out_file name
    base = out_file
    if base.lower().endswith(".svg"):
        base = base[:-4]
    elif base.lower().endswith(".pdf"):
        base = base[:-4]

    dot.render(base, format=out_file.split(".")[-1], cleanup=True)
    print("Wrote:", out_file)

if __name__ == "__main__":
    path = "input.txt"

    adj, nodes = read_graph(path)
    highlight = {
        "svr": "palegreen",
        "out": "lightsalmon",
        "dac": "khaki",
        "fft": "khaki",
    }

    render_graph(adj, nodes, out_file="graph.svg", engine="dot", highlight=highlight, rankdir="LR")
