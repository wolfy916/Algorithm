# 근손실
def dfs(day, muscle):
    global cnt

    if muscle < 500:
        return

    if day == N:
        cnt += 1
    else:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                dfs(day + 1, muscle + kits[i] - K)
                used[i] = 0


N, K = map(int, input().split())
kits = list(map(int, input().split()))
used = [0] * N
cnt = 0
dfs(0, 500)
print(cnt)