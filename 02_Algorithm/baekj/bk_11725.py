# 트리의 부모 찾기

import sys
input = sys.stdin.readline

N = int(input())
adj_List = [[] for _ in '_'*(N+1)]
visited = [0] * (N+1)
par = [0] * (N+1)
for _ in '_'*(N-1):
    a, b = map(int, input().split())
    adj_List[a].append(b)
    adj_List[b].append(a)

q = [1]
visited[1] = 1
while q:
    v = q.pop(0)
    for w in adj_List[v]:
        if not visited[w]:
            visited[w] = 1
            par[w] = v
            q.append(w)

for i in range(2, N+1):
    print(par[i])