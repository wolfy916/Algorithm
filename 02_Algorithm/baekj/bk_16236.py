# 아기 상어
from sys import stdin
input = stdin.readline


def hunt(ii, jj, t_i, t_j):  # ii, jj: 상어, t_i, t_j: 물고기, cnt: 경과 시간
    global N, shark_size
    visited = [[0]*(N+2) for _ in '_'*(N+2)]
    q = [(ii, jj)]
    visited[ii][jj] = 1
    while q:
        i, j = q.pop(0)
        if i == t_i and j == t_j:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if area[ni][nj] != '-' and visited[ni][nj] == 0 and area[ni][nj] <= shark_size:
                q.append((ni, nj))
    return 0


N = int(input())  # N: 2 ~ 20
area = [['-']*(N+2)] + [['-'] + list(map(int, input().split())) + ['-'] for _ in '_'*N] + [['-']*(N+2)]

# 0: 빈칸, 1 ~ 6: 물고기 크기, 9: 아기상어의 위치
# 아기상어의 처음 크기는 2
# 아기상어는  1초마다 상하좌우로 인접한 한 칸씩 이동
# 자신보다 큰 물고기 칸은 지나갈 수 없고, 나머지는 이동 가능
# 크기가 같은 칸은 먹을 수 없지만, 지나갈 수 있음
# 크기가 작으면 먹을 수 있음

# 이동 규칙
# 더 이상 먹을 수 있는 물고기가 없다면 아기 상어는 엄마 상어에게 도움 요청
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 감
# 먹을 수 있는 물고기가 2마리 이상이라면, 가장 가까운 녀석을 먹으러 감
#     거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수가 최솟값이다.
#     거리가 가까운 물고기가 많다면
#     가장 위에 있는 물고기, 그러한 물고기가 여러마리라면
#     가장 왼쪽에 있는 물고기를 먹는다.

# 아기 상어의 이동은 1초가 걸리고, 물고기를 먹는데 걸리는 시간은 없다. 이동과 동시에 먹고, 그 칸은 빈 칸이 된다.
# 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.
# -> 예) 크기가 2인 아기상어는 물고기를 2마리 먹으면 크기가 3이 된다.

# 인덱스 = 물고기들의 크기
fish_n = [0]*7
shark_i = 0
shark_j = 0
shark_size = 2
eat = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if area[i][j] == 9:
            shark_i, shark_j = i, j
        elif area[i][j] != 0:
            fish_n[area[i][j]] += 1

time = 0
while fish_n[:shark_size].count(0) < shark_size:  # 종료 조건 1: 아기상어보다 작은 크기의 물고기들이 한 마리도 없으면 종료
    if sum(fish_n) == 0:
        break
    fish_list = [[] for _ in '_' * 7]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if area[i][j] != 0 and area[i][j] != 9:
                dis = abs(shark_i - i) + abs(shark_j - j)
                fish_list[area[i][j]].append([i, j, dis])

    for i in range(7):
        fish_list[i].sort(key=lambda x: (x[2], x[0], x[1]))

    # 먹잇감 발견
    for k in range(7):
        if fish_n[k] != 0:
            target_i, target_j, target_dis = fish_list[k].pop(0)
            fish_n[k] -= 1
            break

    cnt = hunt(shark_i, shark_j, target_i, target_j)

    if cnt == 0:  # 종료 조건 2: 작은 크기의 물고기가 있지만 갈 수 없으므로 종료
        break
    else:
        area[shark_i][shark_j] = 0
        shark_i, shark_j = target_i, target_j
        area[target_i][target_j] = 0
        area[shark_i][shark_j] = 9

        eat += 1
        time += target_dis
        if eat == shark_size:
            shark_size += 1
            eat = 0
print(time)