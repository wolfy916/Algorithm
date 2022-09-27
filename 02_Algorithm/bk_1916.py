# 최소 비용 구하기

import sys
input = sys.stdin.readline


def dfs(v, sumv):
    global minV

    if minV < sumv:
        return

    elif v == E:
        if minV > sumv:
            minV = sumv

    else:
        for w in adj_List[v]:
            if not visited[w]:
                visited[w] = 1
                dfs(w, sumv + charge[v][w])
                visited[w] = 0


N = int(input())
M = int(input())
adj_List = [[] for _ in '_'*(N+1)]
charge = [[0]*(N+1) for _ in '_'*(N+1)]
for _ in '_'*M:
    s, e, charge[s][e] = map(int, input().split())
    adj_List[s].append(e)
S, E = map(int, input().split())

visited = [0] * (N + 1)
minV = 99999 * M
dfs(S, 0)

print(minV)