# 1256 사전

N, M, K = map(int, input().split())
dp = [[0]*(M+1) for _ in '_'*(N+1)]
for i in range(N+1):
    dp[i][0] = 1
for j in range(M+1):
    dp[0][j] = 1

# 3, 3, 6
# 111000 = 56  1
# 110100 = 52  2
# 110010 = 50  3
# 110001 = 49  4
# 101100 = 44  5
# 101010 = 42  6
# 101001 = 41  7
# 100110 = 38  8
# 100101 = 37  9
# 100011 = 35  10

# 011100 = 28  11
# 011010 = 26  12
# 011001 = 25  13
# 010110 = 22  14
# 010101 = 21  15
# 010011 = 19  16
# 001110 = 14  17
# 001101 = 13  18
# 001011 = 11  19
# 000111 = 7   20

# 56 ~ 7
#