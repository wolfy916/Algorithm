# 트리의 지름

n = int(input())  # 1 ≤ n ≤ 10,000
adjM = [[0]*(n+1) for _ in '_'*(n+1)]
for _ in range(n-1):
    par, chd, value = map(int, input().split())  # 가중치는 100보다 크지 않은 자연수
    adjM[par][chd] = value
    adjM[chd][par] = value


def dfs(s, v):
    global maxV
    visited[s] = 1
    for i in range(1, n+1):
        if adjM[s][i]:
            w = i
            if s < w and not visited[w]:
                dfs(w, v+adjM[s][w])

    if maxV < v:
        maxV = v


maxV = 0
for x in range(1, n):
    visited = [0] * (n + 1)
    dfs(x, 0)
print(maxV)