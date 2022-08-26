T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())

    value = N // P
    rest = N % P
    multiple = value ** (P - rest) * (value + 1) ** rest

    print(f'#{tc} {multiple}')