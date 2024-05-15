# 메이즈 러너
import sys


# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')


# [1] 데이터 입력 및 초기화
N, M, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
users = []
for _ in range(M):
    x, y = map(int, input().split())
    users.append([x - 1, y - 1])
ei, ej = map(int, input().split())
ei -= 1;
ej -= 1;


# [A] 거리 계산
def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


# [B] 인덱스 유효성 검사
def is_valid(ni, nj):
    if ni < 0 or nj < 0 or ni >= N or nj >= N: return True
    return False


# [C] 특정 구역 회전 함수
def rotate(r1, c1, r2, c2):
    global ei, ej
    n = r2 - r1 + 1
    # 회전한 데이터를 저장할 2차원 리스트 생성
    rotated = [[0] * n for _ in range(n)]
    for i in range(r1, r2 + 1):
        ti = i - r1
        for j in range(c1, c2 + 1):
            tj = j - c1
            if maze[i][j] == 0: continue
            rotated[tj][n - 1 - ti] = maze[i][j] - 1

    # 회전한 데이터 미로에 적용
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            maze[i][j] = rotated[i - r1][j - c1]

    # 출구 좌표 회전
    ei, ej = r1 + (ej - c1), c1 + (n - 1 - ei + r1)

    # 회전 구역에 포함된 유저 좌표 회전
    for i in range(M):
        if escape[i]: continue
        ui, uj = users[i]
        if r1 <= ui <= r2 and c1 <= uj <= c2:
            users[i] = [r1 + (uj - c1), c1 + (n - 1 - ui + r1)]


delta1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
delta2 = [(-1, -1), (1, 1)]

answer = 0
time = 0
escape = [False] * M
while time < K and escape.count(False) > 0:
    time += 1

    # 참가자들의 이동
    for i in range(M):
        if escape[i]: continue
        ui, uj = users[i]
        dis = distance(ui, uj, ei, ej)
        for di, dj in delta1:
            ni, nj = ui + di, uj + dj
            if is_valid(ni, nj): continue
            if maze[ni][nj] > 0: continue
            if dis > distance(ni, nj, ei, ej):
                answer += 1
                users[i][0] = ni
                users[i][1] = nj
                if (ni, nj) == (ei, ej):
                    escape[i] = True
                break

    # 모든 참가자들이 탈출했다면 회전할 필요가 없음
    if escape.count(False) < 1:
        break

    # 미로 회전
    tmp = []
    length = 0
    ref = [[0, 0], [0, 0]]  # ref = [exit 기준 좌상단 좌표, exit 기준 우하단 좌표]
    while tmp == []:
        length += 1
        for k in range(2):
            di, dj = delta2[k]
            ref[k][0] = ei + di * length
            ref[k][1] = ej + dj * length
        for i in range(M):
            if escape[i]: continue
            ui, uj = users[i]
            if ref[0][0] <= ui <= ref[1][0] and ref[0][1] <= uj <= ref[1][1]:
                tmp.append((ui, uj))
    for ni in range(ref[0][0], ei + 1):
        for nj in range(ref[0][1], ej + 1):
            if is_valid(ni, nj): continue
            for ui, uj in tmp:
                if ni <= ui <= ni + length and nj <= uj <= nj + length:
                    rotate(ni, nj, ni + length, nj + length)
                    break
            else:
                continue
            break
        else:
            continue
        break

print(answer)
print(ei + 1, ej + 1)