# [S/W 문제해결 기본] 9일차 - 사칙연산
for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in '_'*N]
    chd_left = [0] * 1001
    chd_right = [0] * 1001
    par = [0] * 1001
    tree = [0] * 1001

    for line in arr:
        if len(line) == 2:
            line = list(map(int, line))
            tree[line[0]] = line[1]
        else:
            sign = line.pop(1)
            line = list(map(int, line))
            tree[line[0]] = sign
            chd_left[line[0]] = line[1]
            chd_right[line[0]] = line[2]
            par[line[1]] = par[line[2]] = line[0]

    idx_left = par.index(max(par))
    idx_right = idx_left + 1
    p_idx = par[idx_left]
    while max(par) != 0:
        par[idx_left] = 0
        par[idx_right] = 0

        if tree[p_idx] == '-':
            tree[p_idx] = tree[idx_left] - tree[idx_right]
        elif tree[p_idx] == '+':
            tree[p_idx] = tree[idx_left] + tree[idx_right]
        elif tree[p_idx] == '/':
            tree[p_idx] = tree[idx_left] / tree[idx_right]
        elif tree[p_idx] == '*':
            tree[p_idx] = tree[idx_left] * tree[idx_right]

        idx_left = par.index(max(par))
        idx_right = idx_left + 1
        p_idx = par[idx_left]

    print(f'#{tc} {int(tree[1])}')