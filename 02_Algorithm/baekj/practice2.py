import sys
sys.setrecursionlimit(100000)

def dfs(now):
    if now in gomgom:
        return

    if graph[now] == []:
        print('yes')
        exit()

    for i in graph[now]:
        if i not in gomgom:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

GOM = int(input())
gomgom = list(map(int, input().split()))
dfs(1)
print('Yes')