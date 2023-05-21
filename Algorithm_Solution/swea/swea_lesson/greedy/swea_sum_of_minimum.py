# 최소 합

for tc in range(1, int(input()) + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in '_'*N]

    dx = [1, 0]
    dy = [0, 1]
    minV = 1000

    lenV = 2*N-2
    num = list(range(lenV))
    for i in range(2 ** lenV):
        p = [0] * lenV
        cnt_1 = 0
        for j in range(lenV):
            if i & (1 << j):
                p[num[j]] = 1
                cnt_1 += 1
        if cnt_1 == N-1:
            x = y = 0
            sumV = area[x][y]
            for z in p:
                x, y = x + dx[z], y + dy[z]
                sumV += area[x][y]
            if minV > sumV:
                minV = sumV

    print(f'#{tc} {minV}')