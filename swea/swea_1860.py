# 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # N, M, K(1 ≤ N, M, K ≤ 100)
    nums = list(map(int, input().split()))

    time = 0
    bread = 0
    result = 'Possible'
    while True:

        time += 1
        if time % M == 0:
            bread += K

        customer_num = 0
        repeat = 0
        for customer in nums:
            if customer == time:
                customer_num += 1
            elif customer > time:
                repeat = 1
            elif customer == 0:
                result = 'Impossible'
                repeat = 0
                break

        if bread >= customer_num:
            bread -= customer_num
        else:
            result = 'Impossible'
            break

        if repeat == 0:
            break

    print(f'#{tc} {result}')

