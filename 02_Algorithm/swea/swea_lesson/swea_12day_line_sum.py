T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    area = [list(map(int, input().split())) for _ in '_'*N]

    sumV_list = []
    for i in range(N):
        sumV = 0
        for j in range(i, i+K):
            if 0 <= i < N and 0 <= j < N:
                sumV += area[i][j]
        sumV_list += [sumV]

    maxV = 0
    for x in sumV_list:
        if maxV < x:
            maxV = x

    print(f'#{tc} {maxV}')