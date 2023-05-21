# 최대 상금 (Greedy)
for tc in range(1, int(input()) + 1):
    n, c = input().split()

    c = int(c)
    lenV = len(n)
    arr = [0] * lenV
    for i in range(lenV):
        arr[i] = int(n[i])

    cnt_list = [0] * 10
    for num in arr:
        cnt_list[num] += 1

    check = 0
    check += cnt_list.count(1)
    if check >= lenV:
        check = 0
    else:
        check = 1

    iv_arr = [0] * lenV
    for j, v in enumerate(arr):
        iv_arr[j] = [j, v]
    iv_arr.sort(key=lambda x: x[1], reverse=True)

    fix = [0] * lenV
    change_check = []
    while c != 0:
        for k in range(lenV):
            if fix[k] == 0:
                if k == iv_arr[k][0]:
                    fix[k] = 1
                    continue

                if cnt_list[iv_arr[k][1]] >= 2:
                    Idx = 0
                    for l in range(lenV):
                        if iv_arr[l][1] == iv_arr[k][1]:
                            Idx = iv_arr[l][0]
                    change_check += [[arr[Idx], arr[k], Idx]]
                else:
                    Idx = iv_arr[k][0]

                arr[k], arr[Idx] = arr[Idx], arr[k]
                c -= 1
                fix[k] = 1

                iv_arr = [0] * lenV
                for j, v in enumerate(arr):
                    iv_arr[j] = [j, v]
                iv_arr.sort(key=lambda x: x[1], reverse=True)
                break
        else:
            break

    for i in range(9, 0, -1):
        if cnt_list[i] <= 1:
            continue
        else:
            select = []
            for a, b, j in change_check:
                if not select:
                    if i == a and a > b:
                        select += [[b, j]]
                else:
                    if i == a and a > b:
                        if select[-1][0] > b and select[-1][1] > j:
                            arr[select[-1][1]], arr[j] = arr[j], arr[select[-1][-1]]
                            select += [[b, j]]

    if c % 2 and check == 0:
        arr[-1], arr[-2] = arr[-2], arr[-1]

    result = ''
    for x in arr:
        result += str(x)

    print(f'#{tc} {result}')