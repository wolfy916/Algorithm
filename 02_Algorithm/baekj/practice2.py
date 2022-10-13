# 양팔 저울
from sys import stdin
input = stdin.readline
from itertools import combinations

N = int(input())  # 1 <= 추의 개수 <= 30
weights = list(map(int, input().split()))  # 1g <= 추의 무게 <= 500g
M = int(input())  # 1 <= 구슬의 개수 <= 7
beads = list(map(int, input().split()))  # 1g <= 구슬의 무게 <= 40,000g

dp = [weights] + [[0]*N for _ in '_'*(N-1)]
comb = list(combinations(list(range(N)), 2))
for i, j in comb:
    dp[1][i] = dp[1][j] = dp[0][i] + dp[0][j]

sumV = sum(weights)
end_check = False
check = False
for k in range(2, N):
    for i, j in comb:
        dp[k][i] = dp[k][j] = dp[0][i] + dp[k-1][j]
        if dp[k][i] == sumV:
            end_check = True
            break
    if end_check:
        break

arr = []
for i in range(N):
    arr += dp[i]
arr = set(arr)
arr = list(arr)

for bead in beads:
    in_check = False
    for weight in arr:
        minus = weight - bead
        if minus > 0:
            if minus in arr:
                in_check = True
                break
        elif minus == 0:
            in_check = True
            break

    if in_check:
        print('Y', end=' ')
    else:
        print('N', end=' ')

# for bead in beads:
#     if bead in dp:
#         print('Y', end=' ')
#     else:
#         print('N', end=' ')