# 정식이의 은행 업무

for tc in range(1, int(input()) + 1):
    num_2 = list(map(int, list(input())))
    num_3 = list(map(int, list(input())))

    value_2 = 0
    for i in range(len(num_2) - 1, -1, -1):
        value_2 += num_2[i] * (2 ** (len(num_2) - i - 1))

    num_3_list = [num_3]
    test_3 = num_3.copy()
    if test_3[0] == 1:
        test_3[0] = 2
        num_3_list.append(test_3)
    else:
        test_3[0] = 1
        num_3_list.append(test_3)

    for j in range(1, len(test_3)):
        check = [0, 1, 2]
        check.pop(test_3[j])

        test_3 = num_3.copy()
        test_3[j] = check.pop(0)
        num_3_list.append(test_3)

        test_3 = num_3.copy()
        test_3[j] = check.pop(0)
        num_3_list.append(test_3)

    result = 0
    for num_3_v in num_3_list:
        value_3 = 0
        for k in range(len(num_3_v) - 1, -1, -1):
            value_3 += num_3_v[k] * (3 **(len(num_3_v)-k-1))
        for l in range(len(num_2)-1):
            if abs(value_2 - value_3) == 2**l:
                result = value_3
                break
        if result:
            break

    print(f'#{tc} {result}')