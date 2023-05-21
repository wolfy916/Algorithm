# 10012. 5247. 연산(제출용)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    cnt = [0] * 1000001
    result = abs(M-N)

    q = [N]
    cnt[N] = 1
    while q:
        v = q.pop(0)

        if result <= cnt[v]:
            continue

        if v == M:
            if result > cnt[v]:
                result = cnt[v]

        else:
            for n in range(4):
                delta = [1, -1, v, -10]
                for d in delta:
                    w = v + d
                    if 1 <= w <= 1000000 and not cnt[w]:
                        cnt[w] = cnt[v] + 1
                        q.append(w)

    print(f'#{tc} {result - 1}')