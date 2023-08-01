# 얼음깨기 펭귄
from collections import deque as dq

def bfs(s):
    visited = [0] * (N + 1)
    q = dq([(s, 0)])
    while q:
        v, cnt = q.popleft()
        if v <= S:
            ices[v] = cnt
        else:
            for w in adjL[v]:
                if not visited[w]:
                    visited[w] = 1
                    q.append((w, cnt + 1))


N, S, P = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)

ices = [0] * (S + 1)
bfs(P)
print(N - sum(sorted(ices)[:3]) - 1)
