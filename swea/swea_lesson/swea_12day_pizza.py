T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N : 화덕 크기, M : 피자 개수
    pizza = list(map(int, input().split()))  # 피자

    for i in range(M):  # 피자 번호 부여
        pizza += [[i+1, pizza.pop(0)]]

    q = []  # 화덕 크기만큼 피자 넣기
    for _ in range(N):
        q += [pizza.pop(0)]

    while len(q) != 1:  # 화덕에 피자가 1개만 남을때까지
        cheese = q.pop(0)
        cheese[1] //= 2
        if cheese[1] == 0 and pizza:  # cheese가 다 녹고 피자가 남아있으면
            q += [pizza.pop(0)]
        elif cheese[1] == 0 and not pizza:  # cheese가 다 녹고 피자가 남아있지않으면
            continue
        else:  # cheese가 덜 녹았다면
            q += [cheese]

    print(f'#{tc} {q.pop(0)[0]}')