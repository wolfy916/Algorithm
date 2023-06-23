# 해킹
import sys
input = sys.stdin.readline

def dijkstra(v, INF):
    times[v] = 0  # 출발 노드는 가중치가 없음
    for _ in range(n - 1):
        select_idx = 0
        minV = INF
        for i in range(1, n + 1):
            # 선택하지 않았으며, 해당 노드까지 가는 합산 가중치가 가장 낮은 노드를 선택
            if times[i] < minV and not visited[i]:
                select_idx = i
                minV = times[i]

        visited[select_idx] = 1  # 노드 선택

        for c_idx, time in adjL[select_idx]:
            if not visited[c_idx]:
                # (start -> c_idx) vs (start -> select_idx -> c_idx) 최소 가중치 갱신
                times[c_idx] = min(times[c_idx], times[select_idx] + time)

for tc in range(int(input().rstrip('\n'))):
    n, d, c = map(int, input().rstrip('\n').split())
    INF = 1e7 + 1
    adjL = [[] for _ in range(n + 1)]  # 인접리스트
    for _ in range(d):
        a, b, s = map(int, input().rstrip('\n').split())
        adjL[b].append((a, s))  # 단방향

    visited = [0] * (n + 1)
    times = [INF] * (n + 1)
    dijkstra(c, INF)

    cnt = 0
    maxV = 0
    for i in range(1, n + 1):
        if times[i] != INF:
            cnt += 1
            maxV = max(maxV, times[i])

    print(cnt, maxV)