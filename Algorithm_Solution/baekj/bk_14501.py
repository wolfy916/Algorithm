# 퇴사
N = int(input())
table = [0] + [tuple(map(int, input().split())) for _ in '_'*N]
dp = [0] * (N+2)
for i in range(1, N+1):
    for j in range(i, N+1):
        t, p = table[j]
        test_day = j+t
        if test_day <= N+1:
            dp[test_day] = max(dp[test_day], dp[i] + p)
print(max(dp))