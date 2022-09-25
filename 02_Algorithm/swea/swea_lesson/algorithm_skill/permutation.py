def f(i, N):
    global minV
    global cnt
    cnt += 1
    if i == N:
        s = 0
        for k in range(N):
            s += arr[k][P[k]]       # k행에서 P[k]열 선택
        if minV > s:
            minV = s
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]

def f2(i, s, N):    # i행, s i-1행까지의 합, N 총 행 수
    global minV
    global cnt
    cnt += 1
    if i == N:
        if minV > s:
            minV = s
    elif minV <= s:
        return
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f2(i+1, s+arr[i][P[i]], N)
            P[i], P[j] = P[j], P[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    P = [i for i in range(N)]
    minV = 1000
    cnt = 0
    #f(0, N)
    f2(0, 0, N)
    print(f'#{tc} {minV} {cnt}')