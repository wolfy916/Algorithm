# 쉬운 계단 수

# [A] 메인 로직 함수
def solution(n):
    # dp[i][j] = i-1 자릿수의 마지막 숫자가 j인 경우의 수
    dp = [[0] * 10 for _ in range(n)]

    # 한 자릿수일 때의 경우의 수는 1가지
    # ex) 1, 2, 3, ..., 9
    for j in range(1, 10):
        dp[0][j] = 1

    # 이전 단계의 1차이로 끝난 경우의 수를 합산
    for i in range(1, n):
        for j in range(10):
            if j - 1 >= 0:
                dp[i][j] += dp[i-1][j-1]
            if j + 1 < 10:
                dp[i][j] += dp[i-1][j+1]

    return sum(dp[-1]) % 1000000000

# [main]
if __name__ == '__main__':
    N = int(input())
    print(solution(N))