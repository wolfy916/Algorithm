# 게리맨더링
from itertools import combinations


def check(s, e, area):
    visited = [0]*(N+1)
    q = [s]
    visited[s] = 1
    while q:
        v = q.pop(0)
        if v in adj_L[e]:
            return True
        else:
            for w in adj_L[v]:
                if not visited[w] and w in area:
                    visited[w] = 1
                    q.append(w)
    return False


N = int(input())
populations = [0] + list(map(int, input().split()))
adj_L = [[] for _ in '_'*(N+1)]
for i in range(1, N+1):
    inform = list(map(int, input().split()))
    for adj_sector in inform[1:]:
        adj_L[i].append(adj_sector)
        adj_L[adj_sector].append(i)

minV = 1000
sectors = list(range(1, N+1))
for j in range(1, (N//2)+1):
    area1_lst = list(combinations(sectors, j))
    for area1 in area1_lst:
        break_check = 0
        area2 = []
        sumV2 = 0
        for sector in sectors:
            if sector not in area1:
                area2.append(sector)
                sumV2 += populations[sector]

        for a, b in list(combinations(area1, 2)):
            if not check(a, b, area1):
                break_check = 1
                break

        if break_check:
            continue

        for a, b in list(combinations(area2, 2)):
            if not check(a, b, area2):
                break_check = 1
                break

        if break_check:
            continue

        sumV1 = 0
        for sector in area1:
            sumV1 += populations[sector]

        minusV = abs(sumV1 - sumV2)
        if minV > minusV:
            minV = minusV

if minV == 1000:
    minV = -1

print(minV)