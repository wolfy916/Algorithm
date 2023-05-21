# N-queen

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


def promising(v_i, v_j):
    for i in range(1, N):
        for j in range(8):
            ni, nj = v_i+di[j]*i, v_j+dj[j]*i
            if 0 <= ni < N and 0 <= nj < N and chess[ni][nj] == 1:
                return False
    else:
        chess[v_i][v_j] = 1
        # for i in range(N):
        #     print(*chess[i])
        # print('----------------')
        return True


def check(v_i, v_j, q):
    global cnt

    if promising(v_i, v_j):
        if q == N:
            # for i in range(N):
            #     print(*chess[i])
            # print('카운팅')
            # print('----------------')
            cnt += 1
        else:
            for i in range(N):
                check(v_i+1, i, q+1)
                chess[v_i+1][i] = 0


for tc in range(1, int(input())+1):
    N = int(input())

    cnt = q_cnt = 0
    for i in range(N):
        chess = [[0]*N for _ in '_'*N]
        check(0, i, 1)

    print(f'#{tc} {cnt}')