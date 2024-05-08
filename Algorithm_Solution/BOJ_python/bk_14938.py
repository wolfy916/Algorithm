# 서강그라운드

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
INF = int(10e8)
adjM = [[INF] * (n+1) for _ in '_'*(n+1)]

for i in range(1, n+1):
    adjM[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    adjM[a][b] = min(adjM[a][b], l)
    adjM[b][a] = min(adjM[b][a], l)

for tmp in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            adjM[s][e] = min(adjM[s][tmp] + adjM[tmp][e], adjM[s][e])

answer = 0
for i in range(1, n+1):
    sumV = items[i]
    for j in range(1, n+1):
        if i != j and m >= adjM[i][j]:
            sumV += items[j]
    answer = max(sumV, answer)

print(answer)