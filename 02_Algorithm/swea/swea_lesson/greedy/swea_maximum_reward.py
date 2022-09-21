# 최대 상금
def f(i, k, c):
    global test
    if c == 0 or i == k:
        test += [int(''.join(num))]
    else:
        for j in range(k):
            num[i], num[j] = num[j], num[i]
            cnt = 1 if i != j else 0
            f(i + 1, k, c - cnt)
            num[i], num[j] = num[j], num[i]


for tc in range(1, int(input()) + 1):
    num, count = input().split()
    num = list(num)
    test = []
    f(1, len(num), int(count))
    maxV = list(str(max(test)))

    if len(num) // 2 < int(count) and (int(count) - (len(num) // 2)) % 2:
        maxV[-1], maxV[-2] = maxV[-2], maxV[-1]

    print(f'#{tc} {"".join(maxV)}')