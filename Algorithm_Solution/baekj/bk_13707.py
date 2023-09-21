# 합분해 2
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution(N, K):
    dp = [1] * (N + 1)
    for _ in range(K - 2):
        for i in range(N + 1):
            dp[i] += dp[N - i]
    print(dp)
    return ''

# [main]
if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solution(N, K))