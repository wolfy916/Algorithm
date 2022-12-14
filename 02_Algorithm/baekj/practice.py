# 평범한 배낭
# 조합 완전 탐색 재롱 잔치
from itertools import combinations as cb

N, K = map(int, input().split())
objects = [list(map(int, input().split())) for _ in '_'*N]
maxV = 0
for i in range(1, N+1):
    combs = list(cb(objects, i))
    for comb in combs:
        sumW = sum(map(lambda x: x[0], comb))
        if sumW > K:
            continue
        maxV = max(maxV, sum(map(lambda x: x[1], comb)))
print(maxV)