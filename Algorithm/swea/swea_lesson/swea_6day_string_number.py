T = int(input())
for tc in range(1, T+1):
    s1 = list(input())
    s2 = list(input())

    maxV = 0
    for i in s1:
        cnt = 0
        for j in s2:
            if i == j:
                cnt += 1
        if maxV < cnt:
            maxV = cnt

    print(f'#{tc} {maxV}')
