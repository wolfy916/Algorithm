# 원판 돌리기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def rotate(i, d, k):
    lst = []
    if d:  # 반시계
        for j in range(k+M-1, k-1, -1):
            lst.append(circles[i][j % M])
    else:  # 시계
        for j in range(k, k+M):
            lst.append(circles[i][j % M])

    return lst


N, M, T = map(int, input().split())
circles = [list(map(int, input().split())) for _ in '_' * N]
for _ in '_' * T:
    x, d, k = map(int, input().split())  # d -> 1: 반시계, 0: 시계
    for i in range(N):
        if i % x == 0:
            circles[i] = rotate(i, d, k)
        delete_lst = []
        for j in range(M):
            for di, dj in delta:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and circles[i][j] == circles[ni][nj] > 0:
                    delete_lst.append((ni, nj))
        if delete_lst:
            for del_i, del_j in delete_lst:
                circles[del_i][del_j] = 0
        else:
            avg = sum(circles[i]) / M
            for j in range(M):
                if circles[i][j] > avg:
                    circles[i][j] -= 1
                elif circles[i][j] < avg:
                    circles[i][j] += 1

print(sum(map(sum, circles)))

