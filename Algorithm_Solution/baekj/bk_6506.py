# 엘 도라도
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution(N, K, nums):
    dp = [[0] * (K + 1) for _ in range(N)]
    for i in range(N):
        dp[i][1] = 1
    for i in range(N - 1):
        for j in range(i + 1, N):
            if nums[j] > nums[i]:
                tmp = min(i + 1, K - 1)
                for k in range(1, tmp + 1):
                    dp[j][k+1] += dp[i][k]
    return sum(map(lambda x: x[K], dp))

# [main]
if __name__ == '__main__':
    while True:
        N, K = map(int, input().split())
        if (N, K) == (0, 0): break
        nums = list(map(int, input().split()))
        print(solution(N, K, nums))