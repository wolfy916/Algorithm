# 암호코드 스캔
import sys
sys.stdin = open("sample_input.txt", "r")

D = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9,
}

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 1 <= N < 2000, 1 <= M < 500

    used_code = []
    save_line = ''
    result = 0
    for _ in '_' * N:
        line = input()

        if line == save_line:
            continue
        save_line = line

        if save_line.strip('0'):
            test_nums = []
            test_num = ''
            for x in save_line.strip('0'):
                if x == '0':
                    if len(test_num):
                        test_nums += [test_num]
                    test_num = ''
                    continue

                if x.isnumeric():
                    v = int(x)
                else:
                    v = ord(x) - 55

                for i in range(3, -1, -1):
                    if v & (1 << i):
                        test_num += '1'
                    else:
                        test_num += '0'
            else:
                test_nums += [test_num]

            for test_number in test_nums:

                lenV = len(test_number)

                if lenV <= 52:
                    continue

                test_number = test_number.strip('0')
                while len(test_number) % 56 != 0:
                    test_number = '0' + test_number

                c = len(test_number) // 56

                code = []
                stack = []
                key = ''
                for num in test_number:
                    if len(stack):
                        if stack[-1] != num:
                            key += str(len(stack)//c)
                            stack = [num]
                        else:
                            stack += [num]
                    else:
                        stack += [num]

                    if len(key) == 4:
                        code += [D[key]]
                        key = ''
                else:
                    key += str(len(stack)//c)
                    code += [D[key]]

                sum1 = 0
                sum2 = 0
                for j in range(7):
                    if j % 2:
                        sum2 += code[j]
                    else:
                        sum1 += code[j]

                if (sum1 * 3 + sum2 + code[-1]) % 10 == 0:
                    if code not in used_code:
                        result += sum(code)
                    used_code += [code]

    print(f'#{tc} {result}')