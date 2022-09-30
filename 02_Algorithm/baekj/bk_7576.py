# 토마토
import sys
input = sys.stdin.readline

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

M, N = map(int, input().split())  # 2 <= M(가로), N(세로) <= 1,000
grid_plate = [['-']*(M+2)]+[['-']+list(map(int, input().split()))+['-'] for _ in '_'*N]+[['-']*(M+2)]

q1 = []
unchanged_tomato = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if grid_plate[i][j] == 1:
            q1.append((i, j))
        elif grid_plate[i][j] == 0:
            unchanged_tomato += 1

time = 0
while q1:
    q2 = q1[:]
    q1.clear()
    for vi, vj in q2:
        grid_plate[vi][vj] = -1
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if grid_plate[ni][nj] == 0:
                unchanged_tomato -= 1
                grid_plate[ni][nj] = 1
                q1.append((ni, nj))
    time += 1
else:
    time -= 1

if unchanged_tomato:
    time = -1

print(time)