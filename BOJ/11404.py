N = int(input())
M = int(input())

## adjacency matrix
INF = 1e+10
graph = [[INF]*(N+1) for _ in range(N+1)]

for k in range(N+1):
  graph[k][k] = 0

for _ in range(M):
  v1,v2,w = map(int,input().split())
  graph[v1][v2] = min(graph[v1][v2],w)

for mid in range(1,N+1):
  for src in range(1,N+1):
    if src == mid or graph[src][mid] == INF:
      continue
    for dest in range(1,N+1):
      if dest == mid or dest == src or graph[mid][dest] == INF:
        continue
      if graph[src][dest] > graph[src][mid] + graph[mid][dest]:
        graph[src][dest] = graph[src][mid] + graph[mid][dest]


for i in range(1,N+1):
  for j in range(1,N+1):
    if graph[i][j] != INF:
      print(graph[i][j],end=" ")
    else:
      print("0",end=" ")
  print()
