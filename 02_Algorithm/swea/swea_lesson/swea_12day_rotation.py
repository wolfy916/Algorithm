T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    line = list(map(int, input().split()))

    for i in range(M):
        line += [line.pop(0)]

    print(f'#{tc} {line.pop(0)}')