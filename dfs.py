def dfs_visit(V, Adj, s):
    for v in Adj:
        if v not in parent:
            parent[v] = s
            dfs_visit(V, Adj, v)
def dfs(V, Adj):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            dfs_visit(V, Adj, s)


