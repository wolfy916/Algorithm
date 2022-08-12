T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int, input().split()))

    maxV = line[0]
    minV = line[0]
    maxIdx = 0
    minIdx = 0
    for i in range(0, N):
        if maxV <= line[i]:
            maxV = line[i]
            maxIdx = i
        if minV > line[i]:
            minV = line[i]
            minIdx = i

    if maxIdx >= minIdx:
        result = maxIdx - minIdx
    else:
        result = minIdx - maxIdx

    print(f'#{tc} {result}')