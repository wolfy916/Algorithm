# 5189. 전자카트
def com(a, n):
    global lst
    for i in range(1 << n):
        result = []
        for j in range(n):
            if i & (1 << j):
                result += [a[j]]
        if len(result) == n:
            lst += result


def perm(n, k):
    global comb_list
    if n == k:
        comb_list += [[1] + c + [1]]
    else:
        for i in range(k):
            if used[i] == 0:
                c[n] = lst[i]
                used[i] = 1
                perm(n + 1, k)
                used[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in '_'*N]

    arr = list(range(2, N+1))
    lst = []
    com(arr, N-1)

    c = [0] * (N-1)
    used = [0] * (N-1)
    comb_list = []
    perm(0, N-1)

    minV = 10000000
    for comb in comb_list:
        sumV = 0
        for j in range(N):
            sumV += area[comb[j]-1][comb[j+1]-1]
        if minV > sumV:
            minV = sumV

    print(f'#{tc} {minV}')



