'''
연속합 2 - 백준 골드 5
분류 : DP
'''
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [arr[:] for _ in range(2)]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1] + arr[i], dp[0][i])
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

    print(max(map(max, dp)))