T = int(input())
for tc in range(1, T+1):
    line = list(map(int, input()))

    a = line.copy()
    while True:
        if a == sorted(a, reverse=True):
            break
        if a[0] != max(a):
            maxidx = a.index(max(a))
            a[0], a[maxidx] = a[maxidx], a[0]
            break
        else:
            a = a[1:]

    a = line.copy()
    while True:
        if a == sorted(a, reverse=True):
            break
        if a[0] != max(a):
            maxidx = a.index(max(a))
            a[0], a[maxidx] = a[maxidx], a[0]
            break
        else:
            a = a[1:]

    maxV = ''.join(list(map(str, a)))
    print(f'#{tc} {maxV}')