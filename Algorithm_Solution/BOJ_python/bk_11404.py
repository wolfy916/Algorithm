# 플로이드

# input
n = int(input())
m = int(input())
INF = 10e8
graph = [[INF]*n for _ in '_'*n]

# 출발지와 도착지가 같은 경우는 0 처리
for i in range(n):
    graph[i][i] = 0

# 출발지, 도착지, 버스요금을 넣음
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

# floyd_warshall
for tmp in range(n):
    for s in range(n):
        for e in range(n):
            if graph[s][tmp] + graph[tmp][e] < graph[s][e]:
                graph[s][e] = graph[s][tmp] + graph[tmp][e]

# output
for i in range(n):
    for j in range(n):
        if graph[i][j] >= INF:
            graph[i][j] = 0
    print(*graph[i])