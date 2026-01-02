from io import StringIO
from collections import defaultdict, deque
from util import cstr, COLOR, FORMAT

# inp = StringIO("""\
# svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out
# """)
inp = open("input.txt")

forward_adj = defaultdict(list)
for line in inp:
    fr, to = line.split(": ")
    fr = fr.strip()
    for t in to.split():
        forward_adj[fr].append(t)

def count_paths(adj, source, target):
    nodes = set(adj)
    for u, vs in adj.items():
        for v in vs:
            nodes.add(v)

    # Compute indegree
    indeg = {x: 0 for x in nodes}
    for u, vs in adj.items():
        for v in vs:
            indeg[v] += 1

    # Topological order (Kahn?)
    q = deque([x for x in nodes if indeg[x] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # Make sure this is a DAG
    assert len(topo) == len(nodes)

    # Path counts
    #
    # Go using the topo order, starting with the source node.
    dp = {x: 0 for x in nodes}
    dp[source] = 1
    for u in topo:
        if dp[u] == 0:
            continue
        for v in adj[u]:
            dp[v] += dp[u]

    return dp[target]


svr2fft = count_paths(forward_adj, "svr", "fft")
fft2dac = count_paths(forward_adj, "fft", "dac")
dac2out = count_paths(forward_adj, "dac", "out")
count = svr2fft*fft2dac*dac2out
print(count)

assert(count == 316291887968000)
