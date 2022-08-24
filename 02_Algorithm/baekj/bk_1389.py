def search(s, e, N, c):
    global i
    if area[s][e] == 1:
        return c
    if c != 1 and s == i:
        return 0
    check = []
    for k in range(1, N+1):
        if s == k:
            continue
        if area[s][k] == 1:
            check += [k]
    for new_s in check:
        search(new_s, e, N, c+1)


N, M = map(int, input().split())
relate = [list(map(int, input().split())) for _ in '_' * M]

area = [[0] * (N+1) for _ in '_' * (N+1)]
for x, y in relate:
    area[x][y] = 1
    area[y][x] = 1

result = [0]
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        cnt += search(i, j, N, 1)
    result += [cnt]

print(result.index(min(result)))

