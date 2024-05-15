# 모의 SW 역량 테스트 : 디저트 카페

def dfs(s_i, s_j, cnt, arr, d):
    global max_cnt, i, j

    for k in k_list[d:d+2]:
        ni, nj = s_i+di[k], s_j+dj[k]
        if area[ni][nj] != '-' and area[ni][nj] not in arr:
            if k == d:
                dfs(ni, nj, cnt+1, arr+[area[ni][nj]], d)
            else:
                dfs(ni, nj, cnt+1, arr+[area[ni][nj]], d+1)

        if ni == i and nj == j:
            if max_cnt < cnt:
                max_cnt = cnt


k_list = [0, 1, 2, 3]
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    area = [['-'] + list(map(int, input().split())) + ['-'] for _ in '_'*N]
    area = [['-'] * (N+2)] + area + [['-'] * (N+2)]

    max_cnt = -1
    for i in range(1, N+1):
        for j in range(1, N+1):
            dfs(i, j, 1, [area[i][j]], 0)

    print(f'#{tc} {max_cnt}')


