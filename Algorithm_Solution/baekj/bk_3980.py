# 선발 명단
def dfs(i, v):
    global total_score
    if i == 12:
        if total_score < v:
            total_score = v
    else:
        for j in range(1, 12):
            if not visited[j] and players[i][j]:
                visited[j] = 1
                dfs(i + 1, v + players[i][j])
                visited[j] = 0

for tc in range(int(input())):
    players = [[0]] + [[0] + list(map(int, input().split())) for _ in '_' * 11]
    visited = [0] * 12
    total_score = 0
    dfs(1, 0)
    print(total_score)