T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 5 ≤ N ≤ 100
    arr = list(map(int, input()))  # 0 ≤ ai ≤ 9

    zero_list = [0] * 10
    for x in arr:
        zero_list[x] += 1

    maxV = 0
    Idx = 0
    for i in range(10):
        if maxV <= zero_list[i]:
            maxV = zero_list[i]
            Idx = i

    print(f'#{tc} {Idx} {maxV}')
