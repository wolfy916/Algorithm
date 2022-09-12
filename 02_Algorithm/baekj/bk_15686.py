# 치킨 배달
from sys import stdin
from itertools import combinations

N, M = map(int, input().split())
area = [list(map(int, stdin.readline().split())) for _ in '_' * N]

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            houses += [[i, j]]
        elif area[i][j] == 2:
            chickens += [[i, j]]

combination_idx = list(combinations(range(len(chickens)), M))

result_list = []
for idx_list in combination_idx:
    chicken_distance = 0
    for house in houses:
        house_chicken_distance = 1000
        for idx in idx_list:
            distance = abs(chickens[idx][1] - house[1]) + abs(chickens[idx][0] - house[0])
            if house_chicken_distance >= distance:
                house_chicken_distance = distance
        chicken_distance += house_chicken_distance
    result_list += [chicken_distance]

print(min(result_list))