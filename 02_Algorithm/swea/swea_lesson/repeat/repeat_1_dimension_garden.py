# 1차원 정원

T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())

    water_area = 2*D + 1
    if N % water_area:
        rest = 1
    else:
        rest = 0

    print(f'#{tc} {N//water_area + rest}')