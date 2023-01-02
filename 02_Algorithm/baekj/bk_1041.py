# 주사위
from itertools import combinations as cb

N = int(input())
dice = list(map(int, input().split()))
parallel = [5, 4, 3, 2, 1, 0]
if N == 1:
    print(sum(dice) - max(dice))
    exit()

min_area1 = min(dice)  # 면 1개의 최솟값

min_area2 = 101  # 면 2개 합의 최솟값
area2_combs = list(cb(range(6), 2))
for area2_comb in area2_combs:
    if parallel[area2_comb[0]] in area2_comb:
        continue
    sumV2 = dice[area2_comb[0]] + dice[area2_comb[1]]
    min_area2 = min(min_area2, sumV2)

min_area3 = 151  # 면 3개 합의 최솟값
area3_combs = list(cb(range(6), 3))
for area3_comb in area3_combs:
    check = 0
    for num in area3_comb:
        if parallel[num] in area3_comb:
            check = 1
            break
    if check:
        continue
    else:
        sumV3 = dice[area3_comb[0]] + dice[area3_comb[1]] + dice[area3_comb[2]]
        min_area3 = min(min_area3, sumV3)

if N == 2:
    print(min_area2 * 4 + min_area3 * 4)
else:
    sumV_area1 = min_area1 * ((N - 2) * (N - 2) * 5 + (N - 2) * 4)
    sumV_area2 = min_area2 * ((N - 2) * 8 + 4)
    sumV_area3 = min_area3 * 4
    print(sumV_area1 + sumV_area2 + sumV_area3)