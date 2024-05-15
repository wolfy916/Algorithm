# 로봇 청소기
N, M = map(int, input().split())
r = list(map(int, input().split()))  # 로봇 좌표 : r[0], r[1], 방향 : r[2]
area = [list(map(int, input().split())) for _ in '_'*N]

result = 0  # 청소하는 칸의 개수
di = [-1, 0, 1, 0]  # 0: 북, 1: 동, 2: 남, 3: 서
dj = [0, 1, 0, -1]
while True:
    # 1번 행동 : 현재 위치 청소
    if area[r[0]][r[1]] == 0:
        area[r[0]][r[1]] = 2
        result += 1
    # 2번 행동 준비
    search = r[2]
    check = 0
    while check != 4:
        search -= 1
        if search < 0:
            search = 3
        # 2-1번 행동
        ni, nj = r[0] + di[search], r[1] + dj[search]
        if area[ni][nj] == 0:
            r[2] = search
            r[0], r[1] = ni, nj
            break
        # 2-2번 행동
        else:
            r[2] = search
            check += 1
            continue
    else:
        # 2-3번 행동
        if area[r[0] - di[r[2]]][r[1] - dj[r[2]]] == 2:
            r[0] -= di[r[2]]
            r[1] -= dj[r[2]]
        else:
            # 2-4번 행동
            break

print(result)