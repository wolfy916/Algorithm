# 평범한 배낭
from itertools import combinations as cb

N, K = map(int, input().split())
dp = [0]*(K+1)  # 인덱스 -> 무게, 값 -> 최대 가치
for _ in '_'*N:
    w, v = map(int, input().split())
    dp[w] = max(dp[w], v)

test = []
for i in range(1, ):
