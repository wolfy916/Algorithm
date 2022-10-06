import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())  # 1 ≤ N: 영상 번호, Q: 농부의 질문 개수 ≤ 5,000
adjM = [[0]*(N+1) for _ in '_'*(N+1)]
for _ in '_'*(N-1):
    p, q, r = map(int, input().split())  # 1 ≤ pi, qi ≤ N, 1 ≤ ri ≤ 1,000,000,000
    adjM[p][q] = r
    adjM[q][p] = r

INF = 1000000000
for _ in '_'*Q:
    k, s = map(int, input().split())  # 1 ≤ ki ≤ 1,000,000,000, 1 ≤ vi ≤ N
    cnt = 0
    minV_L = [INF] * (N+1)
    visited = [0] * (N+1)
    q = deque([s])
    visited[s] = 1
    while q:
        v = q.popleft()

        if minV_L[v] < k:
            continue
        elif minV_L[v] >= k and minV_L[v] != INF:
            cnt += 1

        for w in range(1, N+1):
            if adjM[v][w] and not visited[w]:
                q.append(w)
                minV_L[w] = min(minV_L[v], adjM[v][w])
                visited[w] = 1

    # cnt = 0
    # for minV in minV_L:
    #     if minV >= k and minV != INF:
    #         cnt += 1

    print(cnt)