# 장훈이의 높은 선반

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    h_list = list(map(int, input().split()))

    result = []
    for i in range(2 ** N):
        humans = []
        for j in range(N):
            if i & (1 << j):
                humans.append(h_list[j])
        h_humans = sum(humans)
        if h_humans >= B:
            result.append(h_humans)

    print(f'#{tc} {min(result)-B}')