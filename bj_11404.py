import sys

INF = sys.maxsize

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if dist[i][j] > dist[i][k] + dist[k][j]:
#                 dist[i][j] = dist[i][k] + dist[k][j]


n = int(sys.stdin.readline())
graph = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        graph[i][j] = INF
    graph[i][i] = 0

e = int(sys.stdin.readline())
for i in range(e):
    a, b, c = map(int(sys.stdin.readline().split()))
    graph[a][b] = c
print(graph)