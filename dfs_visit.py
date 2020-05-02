# parent = {s: None}
parent = {}
def dfs_visit(Adj, s):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(Adj, v)
