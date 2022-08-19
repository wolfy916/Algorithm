T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    LR_list = [tuple(map(int, input().split())) for _ in '_' * int(Q)]

    box_list = [0] * N
    i = 1
    for L, R in LR_list:
        for box_index in range(L - 1, R):
            box_list[box_index] = i
        i += 1

    print(f'#{tc} {" ".join(list(map(str, box_list)))}')