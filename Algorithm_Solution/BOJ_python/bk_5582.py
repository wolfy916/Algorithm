# 공통 부분 문자열
import sys
input = sys.stdin.readline

str1 = input().rstrip('\n')
str2 = input().rstrip('\n')

lenV1, lenV2 = len(str1), len(str2)
dp = [[0]*lenV2 for _ in '_'*lenV1]
for i in range(lenV1):
    for j in range(lenV2):
        if str1[i] == str2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1]+1

print(max(map(max, dp)))