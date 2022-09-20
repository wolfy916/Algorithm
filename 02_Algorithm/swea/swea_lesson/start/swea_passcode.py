dictionary = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    result = 0
    save_line = 0
    check = 0
    end = 0

    for i in range(N):
        line = input()
        if '1' in line and not check:
            save_line = line
            for j in range(M-1, -1, -1):
                if save_line[j] == '1':
                    end = j
                    break
        if save_line:
            if check <= 4 and save_line == line:
                check += 1

    if end:
        code_list = []
        for k in range(end-55, end+1, 7):
            code = []
            for l in range(k, k+7):
                code += [save_line[l]]
            code = ''.join(code)
            code_list += [dictionary[code]]

        sum1 = 0
        sum2 = 0
        for m in range(8):
            if m % 2:
                sum2 += code_list[m]
            else:
                sum1 += code_list[m]

        if not (sum1*3 + sum2) % 10:
            result = sum1 + sum2

    print(f'#{tc} {result}')