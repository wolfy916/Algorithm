# 포도주 시식
def solution(n, wines):
    dp = [[0, 0, 0] for _ in range(n)]
    if n < 3: return sum(wines)
    dp[0][1] = wines[0]
    dp[1][1] = wines[1]
    dp[1][2] = wines[0] + wines[1]
    for i in range(2, n):
        dp[i][0] += max(dp[i - 1])
        dp[i][1] += wines[i] + max(
            dp[i - 1][0],
            max(dp[i - 2])
        )
        dp[i][2] += wines[i] + max(
            dp[i - 1][1],
            dp[i - 2][0],
        )

    return max(dp[-1])

if __name__ == '__main__':
    n = int(input())
    wines = [int(input()) for _ in range(n)]
    print(solution(n, wines))