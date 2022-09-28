for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    Q = []
    ans = 0
    v = [0] * 1000001
    Q.append((N, 0))

    while Q:
        q = Q.pop(0)
        sub = 2 * q[0]
        cnt = q[1] + 1
        if sub == M:
            ans = cnt
            break
        if sub <= 500000 and not v[sub]:
            Q.append((sub, cnt))
            v[sub] = 1

        sub = q[0] - 10
        if sub == M:
            ans = cnt
            break
        if sub > 10 and not v[sub]:
            Q.append((sub, cnt))
            v[sub] = 1

        sub = q[0] - 1
        if sub == M:
            ans = cnt
            break
        if sub > 1 and not v[sub]:
            Q.append((sub, cnt))
            v[sub] = 1

        sub = q[0] + 1
        if sub == M:
            ans = cnt
            break
        if sub < 1000000 and not v[sub]:
            Q.append((sub, cnt))
            v[sub] = 1

    print(f'#{t}', cnt)