# 프렉탈 평면

# [A] 해당 위치에 대한 0, 1을 반환하는 재귀함수
def fractal(length, vi, vj):
    # [A-1] 하위 조건(검정색 영역)에 걸리지 않고,
    #       length가 1이 된다면 하얀색 영역으로 판단
    if length == 1:
        return '0'

    # [A-2] 검정색 영역 판별 조건
    div = length // N
    black = (length - K * div) // 2
    i_init = vi // length
    j_init = vj // length
    if i_init * length + black <= vi < i_init * length + black + K * div:
        if j_init * length + black <= vj < j_init * length + black + K * div:
            return '1'

    return fractal(length // N, vi, vj)

s, N, K, R1, R2, C1, C2 = map(int, input().split())
L = N ** s
for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        print(fractal(L, i, j), end='')
    print()
