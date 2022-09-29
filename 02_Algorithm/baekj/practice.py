

def dijkstra(N):
    D = adj_M[S][:]
    U = []
    for _ in '_'*(N+1):
        w = 0
        minV = INF
        for i in range(N+1):
            if i not in U and minV > D[i]:
                w = i
                minV = D[i]
        U.append(w)
        for v in range(N+1):
            if 0 < adj_M[w][v] < INF:
                D[v] = min(D[v], D[w] + adj_M[w][v])
    return D[N]


N = int(input())
M = int(input())
INF = 10000000
adj_M = [[INF]*(N+1) for _ in '_'*(N+1)]

for i in range(N+1):
    adj_M[i][i] = 0

for _ in '_'*M:
    s, e, adj_M[s][e] = map(int, input().split())

S, E = map(int, input().split())

print(dijkstra(E))