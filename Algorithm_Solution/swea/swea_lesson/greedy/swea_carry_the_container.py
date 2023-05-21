# 컨테이너 운반

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)

    use_t = [0] * M
    result = 0
    for w_i in w:
        for i, t_i in enumerate(t):
            if w_i <= t_i and use_t[i] == 0:
                use_t[i] = 1
                result += w_i
                break

    print(f'{tc} {result}')