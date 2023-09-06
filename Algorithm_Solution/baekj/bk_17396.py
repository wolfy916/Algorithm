# 백도어
import sys
from heapq import heappop, heappush

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] bfs + 우선 순위큐
def bfs(N, vision, adjL):
    INF = float('inf')
    dis = [INF] * N
    dis[0] = 0
    q = [(0, 0)]
    while q:
        t1, v = heappop(q)
        if v == N - 1: break
        if dis[v] < t1: continue
        for w, t2 in adjL[v]:
            if vision[w]: continue
            tmp = t1 + t2
            if dis[w] <= tmp: continue
            dis[w] = tmp
            heappush(q, (tmp, w))
    return -1 if dis[-1] == INF else dis[-1]

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    vision = list(map(int, input().split()))
    vision[-1] = 0
    adjL = [[] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        adjL[a].append((b, t))
        adjL[b].append((a, t))
    print(bfs(N, vision, adjL))