# 최소 생산 비용 (제출용)
def perm(k, r, lenv, sum_v):
    global minV
    if minV < sum_v:
        return

    elif k == r:
        if minV > sum_v:
            minV = sum_v

    else:
        for i in range(lenv):
            if used[i] == 0:
                used[i] = 1
                p[k] = i
                perm(k+1, r, lenv, sum_v+table[k][p[k]])
                used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in '_'*N]

    minV = 99*N
    p = [0] * N
    used = [0] * N
    perm(0, N, N, 0)

    print(f'#{tc} {minV}')

