# 쿼드 트리
def quadTree(si, sj, ei, ej):
    if si == ei and sj == ej:
        return str(video[si][sj])
    else:
        m1, m2 = (si+ei)//2, (sj+ej)//2
        delta_i = [(si, m1+1), (m1+1, ei+1)]
        delta_j = [(sj, m2+1), (m2+1, ej+1)]
        temp = "("
        for k in range(4):
            start_i, end_i = delta_i[0] if k < 2 else delta_i[1]
            start_j, end_j = delta_j[k % 2]
            temp += quadTree(start_i, start_j, end_i-1, end_j-1)

        if ("0000" in temp) or ("1111" in temp):
            return temp[1]
        else:
            return temp + ")"

N = int(input())
video = [list(map(int, input())) for _ in '_'*N]
print(quadTree(0, 0, N-1, N-1))