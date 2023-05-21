# 새로운 게임
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]

N, K = map(int, input().split())
area = [list(map(int, input().split())) for _ in '_'*N]
pieces = []
location = [[[] for _ in '_'*N] for _ in '_'*N]
for num in range(1, K+1):
    i, j, d = list(map(int, input().split()))
    pieces.append([i-1, j-1, d-1])
    location[i-1][j-1].append(num)

turn = 0
check = 0
while turn < 1000:
    turn += 1
    for n in range(1, N+1):
        i, j = pieces[n-1][0], pieces[n-1][1]
        if location[i][j][0] == n:
            di, dj = delta[pieces[n-1][2]]
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if area[ni][nj] == 0:
                    location[ni][nj] += location[i][j][:]
                    for m in location[i][j]:
                        pieces[m-1][0], pieces[m-1][1] = ni, nj
                    location[i][j].clear()
                elif area[ni][nj] == 1:
                    location[ni][nj] += location[i][j][::-1]
                    for m in location[i][j]:
                        pieces[m-1][0], pieces[m-1][1] = ni, nj
                    location[i][j].clear()
                elif area[ni][nj] == 2:
                    pieces[n - 1][2] = delta.index((-di, -dj))
                    if 0 <= i - di < N and 0 <= j - dj < N:
                        if area[i-di][j-dj] == 0:
                            location[i-di][j-dj] += location[i][j][:]
                            for m in location[i][j]:
                                pieces[m - 1][0], pieces[m - 1][1] = i-di, j-dj
                            location[i][j].clear()
                        elif area[i-di][j-dj] == 1:
                            location[i-di][j-dj] += location[i][j][::-1]
                            for m in location[i][j]:
                                pieces[m - 1][0], pieces[m - 1][1] = i-di, j-dj
                            location[i][j].clear()
            else:
                pieces[n - 1][2] = delta.index((-di, -dj))
                if area[i - di][j - dj] == 0:
                    location[i - di][j - dj] += location[i][j][:]
                    for m in location[i][j]:
                        pieces[m - 1][0], pieces[m - 1][1] = i - di, j - dj
                    location[i][j].clear()
                elif area[i - di][j - dj] == 1:
                    location[i - di][j - dj] += location[i][j][::-1]
                    for m in location[i][j]:
                        pieces[m - 1][0], pieces[m - 1][1] = i - di, j - dj
                    location[i][j].clear()

        if len(location[pieces[n-1][0]][pieces[n-1][1]]) >= 4:
            check = 1
            break

    if check:
        break

else:
    turn = -1

print(turn)