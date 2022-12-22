# 인수의 생일 파티

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    # 플로이드 워셜 풀이 - 제한시간 초과
    # INF = 10000000
    # adjM = [[INF]*N for _ in '_'*N]
    # for i in range(N):
    #     adjM[i][i] = 0
    # for _ in range(M):
    #     x, y, c = map(int, input().split())
    #     adjM[x-1][y-1] = min(adjM[x-1][y-1], c)
    # for k in range(N):
    #     for i in range(N):
    #         for j in range(N):
    #             adjM[i][j] = min(adjM[i][j], adjM[i][k] + adjM[k][j])
    #
    # for i in range(N):
    #     for j in range(N):
    #         if adjM[i][j] >= INF:
    #             adjM[i][j] = 0
    # maxV = 0
    # for i in range(N):
    #     sumV = adjM[X-1][i] + adjM[i][X-1]
    #     maxV = max(maxV, sumV)
    # print(f'#{tc} {maxV}')

    # 다잌스트라 풀이
    def dijkstra(N, X, adj, d):
        d[X] = 0
        for i, c in adj[X]:
            d[i] = c
        U = [X]
        for _ in range(N - 1):  # N개의 정점 중 출발을 제외한 정점 선택
            w = 0
            for i in range(1, N + 1):
                if (i not in U) and d[i] < d[w]:  # 남은 노드 중 비용이 최소인 w
                    w = i
            U.append(w)
            for v, c in adj[w]:
                d[v] = min(d[v], d[w] + c)

    adj = [[] for _ in range(N + 1)]
    adj_reverse = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x].append((y, c))
        adj_reverse[y].append((x, c))
    from_X_to_i = [1000000]*(N+1)
    from_i_to_X = [1000000]*(N+1)
    dijkstra(N, X, adj, from_X_to_i)
    dijkstra(N, X, adj_reverse, from_i_to_X)
    # print(from_X_to_i)
    # print(from_i_to_X)

    maxV = 0
    for i in range(1, N+1):
        maxV = max(maxV, from_X_to_i[i] + from_i_to_X[i])
    print(f'#{tc} {maxV}')