# 원판 돌리기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def rotate(i, d, k):
    lst = circles[i][:]
    if d:  # 반시계
        for _ in '_' * k:
            lst.append(lst.pop(0))
    else:  # 시계
        for _ in '_' * k:
            lst = [lst.pop()] + lst
    return lst


N, M, T = map(int, input().split())
circles = [list(map(int, input().split())) for _ in '_' * N]
zero_num = 0
for _ in '_' * T:
    x, d, k = map(int, input().split())  # d -> 1: 반시계, 0: 시계
    for ii in range(N):
        if ii % x == 0:
            circles[ii] = rotate(ii, d, k)
    delete_lst = []
    for i in range(N):
        for j in range(M):
            for di, dj in delta:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and circles[i][j] == circles[ni][nj] > 0:
                    delete_lst.append((ni, nj))
    if delete_lst:
        for del_i, del_j in delete_lst:
            circles[del_i][del_j] = 0
            zero_num += 1
    else:
        avg = sum(map(sum(circles))) / (N*M - zero_num)
        for i in range(N):
            for j in range(M):
                if circles[i][j] > avg:
                    circles[i][j] -= 1
                elif circles[i][j] < avg:
                    circles[i][j] += 1

print(sum(map(sum, circles)))

