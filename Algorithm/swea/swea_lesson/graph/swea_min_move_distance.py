# 10019. 5251. 최소 이동 거리(제출용)

# 다잌스트라 풀이

def dijkstra(N):
    D = adjM[0][:]  # D <- adjM[s] s에서 출발해 다른 정점으로 가는 초기비용
    U = []          # U = [s] 비용이 결정된 정점 집합, 출발점 s는 비용 확정
    for _ in '_'*(N+1):  # 출발점을 제외한 N개 정점에 대해 비용 결정 , while U != V:
        w = 0
        minV = INF
        for i in range(N+1):  # 아직 비용이 결정되지 않은 정점 중 D[w]가 최소인 w 찾기
            if i not in U and minV > D[i]:
                w = i
                minV = D[i]

        U.append(w)
        for v in range(N+1):  # w와 인접인 정점 v에 대해
            if 0 < adjM[w][v] < INF:  # 자기 자신이 아니며, 인접한 정점 v에 대해
                D[v] = min(D[v], D[w] + adjM[w][v])  # 기존에 v로 가는 비용보다 w를 경유해 가는 비용이 더 적으면
    return D[N]


T = int(input())
INF = 1000000
for tc in range(1, T+1):
    N, E = map(int, input().split())  # 마지막
    V = N + 1  # 정점 수
    adjM = [[INF]*V for _ in range(V)]

    for i in range(V):
        adjM[i][i] = 0
    for _ in '_'*E:
        s, e, w = map(int, input().split())
        adjM[s][e] = w

    print(f'#{tc} {dijkstra(N)}')

