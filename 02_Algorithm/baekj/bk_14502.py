# 연구소

N, M = map(int, input().split())  # 3 ≤ N, M ≤ 8
area = [[1] * (M + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in '_' * N] + [[1] * (M + 2)]

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

lst = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if not area[i][j]:
            lst.append((i, j))


def bfs(si, sj):
    global sample
    q = [(si, sj)]
    while q:
        vi, vj = q.pop(0)
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if not sample[ni][nj]:
                sample[ni][nj] = 2
                q.append((ni, nj))


from itertools import combinations
combs = tuple(combinations(lst, 3))

maxV = 0
for comb in combs:
    sample = [x[:] for x in area]
    for ci, cj in comb:
        sample[ci][cj] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if sample[i][j] == 2:
                bfs(i, j)
    sumV = 0
    for line in sample:
        sumV += line.count(0)
    if maxV < sumV:
        maxV = sumV

print(maxV)