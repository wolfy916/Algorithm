# 1251. 4일차 - 하나로

def dijkstra(n):
    global E
    D = [INF]*N
    D[0] = 0
    U = []
    for _ in '_'*N:
        Idx = 0
        minV = INF
        for i in range(N):
            if i not in U and minV > D[i]:
                Idx = i
                minV = D[i]
        U.append(Idx)
        for j in range(N):
            if j not in U:
                D[j] = min(D[j], ((abs(x[Idx]-x[j])**2)+(abs(y[Idx]-y[j])**2))*E)
    return sum(D)

INF = 10**18
T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N: 섬의 개수, 1 <= N <= 1000

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    print(f'#{tc} {round(dijkstra(0))}')