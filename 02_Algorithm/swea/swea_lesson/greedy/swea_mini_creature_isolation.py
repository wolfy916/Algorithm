# 모의 SW 역량 테스트 : 미생물 격리

di = [0, -1, 1, 0, 0, 0]
dj = [0, 0, 0, 0, -1, 1]
t = [0, 1, 2, 4, 5]
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())  # N: 한 변의 셸의 개수, M: 격리 시간, K: 미생물 군집의 개수

    area = [[0]*N for _ in '_'*N]
    virus = [0]*(K+1)
    fixed = [0]*(K+1)
    direction = [0]*(K+1)
    for i in range(1, K+1):
        vi, vj, vn, vd = map(int, input().split())
        virus[i] = vn
        direction[i] = vd
        area[vi][vj] = i  # vn: 미생물 군집수, vd: 방향값, fix: 행동을 완료하고 고정상태 설정

    while M:
        M -= 1
        for i in range(N):
            for j in range(N):
                if area[i][j] != 0:
                    v = area[i][j]
                    ni, nj = i+di[t[direction[v]]], j+dj[t[direction[v]]]  # 여기로 이동할거임
                    v2 = area[ni][nj]
                    if v2 != 0: # 이동할 공간에 미생물 있음
                        if fixed[v2]:  # fix상태임 -> 합체처리 시작 (sum(미생물수), 방향은 미생물수가 큰쪽을 상속)
                            if virus[v2] > virus[v]:
                                vd = direction[v2]
                            else:
                                vd = direction[v]
                            area[ni][nj] = v2
                            virus[v2] += virus[v]
                            virus[v] = 0
                            direction[v2] = vd

                        elif not fixed[v2] and abs(t[direction[v2]] - t[direction[v]]) == 1: # unfix 상태 -> 상호 교환처리 시작
                            area[i][j], area[ni][nj] = v2, v
                            fixed[v] = 1
                            fixed[v2] = 1

                    else: # 이동할 공간에 미생물 없음 정상이동 처리
                        area[ni][nj] = v
                        area[i][j] = 0

                    # 약품 구역 확인(미생물수//2, 방향 반대)
                    if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
                        for k in range(1, 5):
                            if abs(t[direction[v2]] - t[direction[v]]) == 1:
                                direction[v2] = k
                        virus[v2] //= 2

                    # fix 처리
                    fixed[v2] = 1
                    fixed[v] = 1
                    print('---------------------------')
                    for l in area:
                        print(*l)
                    print('----------------------------')
        fixed = [0]*(K+1)

    result = sum(virus)

    print(f'#{tc} {result}')