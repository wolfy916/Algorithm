# 아기 상어
from sys import stdin
input = stdin.readline


def bfs(s_i, s_j):  # s_i, s_j: 아기 상어 현재 위치
    global shark_size
    if s_i == 4 and s_j == 8:
        a = 1
    visited = [[0]*(N+2) for _ in '_'*(N+2)]  # visited 생성
    q = [[s_i, s_j, 0]]    # 상어 좌표 인큐
    visited[s_i][s_j] = 1  # 상어 좌표 visited
    food = 0               # 리턴할 변수 생성
    while q:
        i, j, k = q.pop(0)  # i, j: 방문한 곳의 좌표, k: 방문한 곳까지의 거리

        if 0 < area[i][j] < shark_size and area[i][j] != 9:  # 상어가 아니며, 상어보다 작은 물고기이면
            if food:  # 먹잇감 우선순위 적용하여 갱신 : 가까운 거리 > 위쪽 > 왼쪽
                if food[2] == k:
                    if food[0] == i:
                        if food[1] > j:
                            food = [i, j, k]
                    elif food[0] > i:
                        food = [i, j, k]
                elif food[2] > k:
                    food = [i, j, k]
            else:  # 먹잇감이 아직 정해지지 않았다면 바로 할당
                food = [i, j, k]

        # bfs 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if food and food[2] < k+1:  # 먹잇감 후보가 존재할 때, 새로 탐색하려는 곳의 거리가 더 멀다면 인큐없이 for문 종료
                break
            if area[ni][nj] != '-' and visited[ni][nj] == 0 and area[ni][nj] <= shark_size:
                visited[ni][nj] = 1      # 탐색할 곳 visited
                q.append([ni, nj, k+1])  # 탐색할 곳 인큐

    return food  # 탐색을 다 돌면 리턴


N = int(input())  # N: 2 ~ 20, N x N 2차원 리스트
area = [['-']*(N+2)] + [['-'] + list(map(int, input().split())) + ['-'] for _ in '_'*N] + [['-']*(N+2)]

fish_n = [0]*7  # 물고기 크기를 인덱스로 받은 남은 물고기 수 리스트
shark_i = shark_j = 0  # 상어 좌표
shark_size = 2         # 상어 사이즈
eat = 0                # 상어가 먹방한 물고기 수

# 상어 인덱스 탐색 및 물고기 사이즈별로 카운트
for i in range(1, N+1):
    for j in range(1, N+1):
        if area[i][j] == 9:
            shark_i, shark_j = i, j  # 상어 인덱스 저장
        elif area[i][j] != 0:
            fish_n[area[i][j]] += 1  # 물고기 수 저장

time = 0  # 시간 초기값
while fish_n[:shark_size].count(0) < shark_size:  # 조건 1. 상어 사이즈보다 작은 크기의 물고기들이 하나도 없다면 종료

    # 진행 상황을 확인할 수 있는 코드
    ########################################################################
    # for i in range(N+2):
    #     print(*area[i])
    # else:
    #     print(f'상어 크기: {shark_size}, 물고기 먹은 수: {eat}, 시간: {time}')
    #     print('.................................................')
    ##########################################################################

    # 현재 상어 위치에서 먹방할 수 있는 가장 가까운 물고기의 좌표(i, j)와 거리(k) 계산
    fish = bfs(shark_i, shark_j)

    # 먹잇감이 있다면 좌표 할당하고 먹방 진행
    if fish:
        fish_i, fish_j, fish_dis = fish
        fish_n[area[fish_i][fish_j]] -= 1  # 먹힌 물고기 수 제외
    # 종료 조건2. 탐색 후에 상어보다 작은 크기의 물고기가 있더라도 갈 수 없다면 종료
    else:
        break

    # 좌표값 최신화
    area[shark_i][shark_j] = 0         # 기존 상어 위치값 9 -> 0
    area[fish_i][fish_j] = 9           # 잡아 먹힌 물고기 위치값 (물고기 사이즈) -> 9(상어)
    shark_i, shark_j = fish_i, fish_j  # 좌표 교환
    eat += 1            # 1 마리 먹방
    time += fish_dis  # 이동 거리(=이동 시간) 합산
    if eat == shark_size:  # 물고기 크기와 먹은 물고기 수가 같다면
        shark_size += 1    # 사이즈 up
        eat = 0            # 먹방한 물고기 수 초기화

# 종료 직전 상황을 확인 할 수 있는 코드
########################################################################
# for i in range(N+2):
#     print(*area[i])
# else:
#     print(f'상어 크기: {shark_size}, 물고기 먹은 수: {eat}, 시간: {time}')
#     print('.................................................')
##########################################################################

print(time)