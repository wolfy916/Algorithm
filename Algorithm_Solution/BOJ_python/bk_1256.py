# 사전
# DP 풀이
N, M, K = map(int, input().split())

# dp[i][j] = a의 개수 i개와 z의 개수 j개를 사용하여 만들 수 있는 문자열 개수
# dp[i][0] = 1, dp[0][1] = 1로 초기화 해둘 수 있고
# dp[i][j] = dp[i-1][j] + dp[i][j-1]임을 이용한다.
dp = [[1]*(M+1) for _ in '_'*(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[N][M] < K:
    print(-1)
else:
    result = ""
    while True:
        # N 혹은 M이 0이 되었다면
        if not N or not M:
            result += "z"*M
            result += "a"*N
            break

        flag = dp[N-1][M]
        if K <= flag:
            result += "a"
            N -= 1
        else:
            result += "z"
            M -= 1
            K -= flag
    print(result)