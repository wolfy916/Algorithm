# 나무 탈출
import sys
sys.setrecursionlimit(10**5)

def dfs(n):
    global cnt, result
    visited[n] = 1
    for x in adjList[n]:
        if visited[x] == 0:  # 방문하지 않은 x
            cnt += 1
            dfs(x)
            if len(adjList[x]) == 1:
                result += cnt
            cnt -= 1


input = sys.stdin.readline
N = int(input())  # 노드 수
E = N - 1  # 간선 수
adjList = [[] for _ in '_' * (N+1)]
for _ in '_' * (N-1):
    a, b = map(int, input().split())
    adjList[a] += [b]
    adjList[b] += [a]

cnt = 0
result = 0
visited = [0] * (N+1)
dfs(1)

if result % 2:
    print('Yes')
else:
    print('No')