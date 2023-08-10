# 도시 왕복하기
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

N, P = map(int, input().split())
adjM = [[[0, 0] for _ in range(N+2)] for _ in range(N+2)]
for _ in range(P):
    a, b = map(int, input().split())
    adjM[a][b][1] = 1
adjM[0][1][1] = 1e9
adjM[2][N+1][1] = 1e9

def dfs(v):
    if v == N + 1:
        return True
    for i in range(N + 2):
        if visited[i]: continue
        if adjM[v][i][1] - adjM[v][i][0] <= 0: continue
        adjM[v][i][0] += 1
        if i != 0:
            adjM[i][v][0] -= 1
        visited[i] = True
        if dfs(i):
            visited[i] = False
            return True
        adjM[v][i][0] -= 1
        if i != 0:
            adjM[i][v][0] -= 1
        visited[i] = False
    return False

visited = [False] * (N + 2)
visited[0] = True
while dfs(0):
    pass
print(adjM[2][N+1][0])