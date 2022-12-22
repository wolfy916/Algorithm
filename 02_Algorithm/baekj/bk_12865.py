# 평범한 배낭
# knapsack DP의 대표 문제
N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in '_'*(N+1)]
for i in range(1, N+1):
    w, v = map(int, input().split())
    if w <= K:
        dp[i][w] = v
    for j in range(1, K+1):
        if j > w:
            dp[i][j] = max(dp[i][j], dp[i-1][j], v + dp[i-1][j-w])
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
print(dp[-1][-1])