# 최소 비용 구하기
# 다이크스트라

import sys
input = sys.stdin.readline

def dijkstra(start):
    # 시작 정점의 최소 비용은 0
    costs[start] = 0

    # 시작정점을 제외한 나머지 N - 1개의 정점에 대해 최소비용을 구함
    for _ in range(N - 1):
        u = 0
        minV = INF
        for i in range(1, N + 1):
            # 가장 낮은 최소 비용의 정점을 선택
            if costs[i] < minV and not visited[i]:
                u = i
                minV = costs[i]

        visited[u] = 1  # 선택

        for i in range(1, N + 1):
            # 선택한 정점과 연결된 선택되지 않은 노드라면
            if adjM[u][i] != INF and not visited[i]:
                # S -> i로 가는 기존의 비용보다
                # S -> u -> i로 가는 비용이 더 작다면
                if costs[i] > costs[u] + adjM[u][i]:
                    costs[i] = costs[u] + adjM[u][i]  # 갱신

N = int(input().rstrip('\n'))
M = int(input().rstrip('\n'))
INF = 1e8 + 1
adjM = [[INF] * (N + 1) for _ in '_' * (N + 1)]
costs = [INF] * (N + 1)
visited = [0] * (N + 1)
for _ in '_' * M:
    s, e, c = map(int, input().rstrip('\n').split())
    adjM[s][e] = min(adjM[s][e], c)
S, E = map(int, input().rstrip('\n').split())
if S != E:
    dijkstra(S)
    print(costs[E])
else:
    print(0)