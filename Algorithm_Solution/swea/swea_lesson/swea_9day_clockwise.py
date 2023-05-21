def clockwise(area_n):  # 2차원 정방행렬을 매개변수로 받아 90도 시계방향으로 회전 시키는 함수
    global N
    rotated_area = []
    for j in range(N):
        stack = []
        for i in range(N-1, -1, -1):
            stack += [area_n[i][j]]
        rotated_area += [''.join(list(map(str, stack)))]
    return rotated_area


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in '_' * int(N)]

    area_90 = clockwise(area)
    area_180 = clockwise(area_90)
    area_270 = clockwise(area_180)

    print(f'#{tc}')
    for k in range(N):
        print(area_90[k], area_180[k], area_270[k])