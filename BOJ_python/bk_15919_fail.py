# 사자는 여행왕이야!
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

N = int(input())
M = int(input())
schedules = [list(map(int, input().split())) for _ in range(M)]
schedules.sort()
dp = [N] * (N + 1)
dp[0] = 0
for a, b in schedules:
    for i in range()
        dp[b] = min(dp[b], max(dp[i], a-i-1))

print()