# 구간 합 구하기 5
N, M = map(int, input().split())
grid = [[0]*(N+1)]+[[0] + list(map(int, input().split())) for _ in '_'*N]

for i in range(1, N+1):
    for j in range(1, N+1):
        grid[i][j] += grid[i][j-1]
        grid[j][i] += grid[j-1][i]

# for j in range(1, N+1):
#     for i in range(1, N+1):
#         grid[i][j] += grid[i-1][j]

for _ in '_'*M:
    x1, y1, x2, y2 = map(int, input().split())
    print(grid[x2][y2] - grid[x2][y1-1] - grid[x1-1][y2] + grid[x1-1][y1-1])