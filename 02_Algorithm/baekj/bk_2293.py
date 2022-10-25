# 동전 1
n, k = map(int, input().split())
dp = [0]*100001
for _ in '_'*n:
    value = int(input())
    dp[value] += 1
    for i in range(value, k+1):
        dp[i] += dp[i-value]
print(dp[k])