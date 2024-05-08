# 줄 세우기
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] LIS의 길이를 계산하는 함수
def cal_LIS_length(arr, N):
    dp = [1] * N
    for i in range(1, N):
        tmp = 0
        for j in range(i):
            if arr[j] < arr[i]:
                if tmp < dp[j]:
                    tmp = dp[j]
        dp[i] = tmp + 1
    return max(dp)

# [main]
if __name__ == '__main__':
    N = int(input())
    kids = [int(input()) for _ in range(N)]
    max_length = cal_LIS_length(kids, N)
    print(N - max_length)