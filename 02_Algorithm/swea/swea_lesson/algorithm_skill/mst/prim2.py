# MST.에 포함된 정점과 인접한 정점 중 가중치가 최소인 정점을 고르는 방식
def prim2(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    MST[r] = 1          # 시작정점 표시
    s = 0               # MST 간선의 가중치 합
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):    # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않고 가중치가 최소인 정점 u찾기
            if MST[i]==1:
                for j in range(V+1):
                    if adjM[i][j]>0 and MST[j]==0 and minV>adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s

V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프

print(prim2(0, V))