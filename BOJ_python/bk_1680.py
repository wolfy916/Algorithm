# 쓰레기 분리수거

T = int(input())
for tc in range(1, T+1):
    W, N = map(int, input().split())  # W : 최대 적재량, N : 쓰레기가 있는 장소 수
    x_and_w = [list(map(int, input().split())) for _ in '_' * N]

    move_distance = 0  # 이동거리
    garbage_load = 0   # 현재 적재량
    for x, w in x_and_w:
        if garbage_load + w < W:
            garbage_load += w
        elif garbage_load + w == W:
            move_distance += 2 * x
            garbage_load = 0
        elif garbage_load + w > W:
            move_distance += 2 * x
            garbage_load = w

    if garbage_load:
        move_distance += 2 * x

    print(move_distance)