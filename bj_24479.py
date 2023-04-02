import sys

def dfs(graph, v, visited):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    print(visited)
nvertex, edge, snode = map(int, sys.stdin.readline().split())
graph = []
for i in range(edge):
    graph.append(list(map(int, sys.stdin.readline().split())))
print(graph)

visited = [False] * nvertex
dfs(graph, snode, visited)