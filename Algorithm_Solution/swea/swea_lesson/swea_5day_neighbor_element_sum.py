T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    maxV = 0
    for i in range(N):
        for j in range(N):
            sumV = 0
            for k in range(4):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:
                    sumV += area[i+di[k]][j+dj[k]]
            if maxV < sumV:
                maxV = sumV

    print(f'#{tc} {maxV}')