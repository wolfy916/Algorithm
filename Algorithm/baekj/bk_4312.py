while True:
    num = int(input())
    if num == 0:
        break
    len_var = 0
    for x in range(num):
        if 2**x > num:
            len_var = x
            break

    line = [3**y for y in range(len_var)]

    n = len(line)
    test_list = []
    for i in range(1<<n):
        sum_list = []
        for j in range(n):
            if i & (1<<j):
                sum_list += [line[j]]
        test_list.append(sum_list)
    test_list = sorted(test_list, key=lambda x:sum(x))

    print('{ ',end='')
    for z in test_list[num-1]:
        if test_list[num-1][-1] == z:
            print(f'{z}',end=' ')
        else:
            print(f'{z}',end=', ')
    print('}')


