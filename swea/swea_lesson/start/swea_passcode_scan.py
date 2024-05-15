# 암호코드 스캔
import sys
sys.stdin = open("sample_input.txt", "r")

D = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
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

        if line.strip('0'):
            test_line = ''
            for x in line.strip('0'):

                if x.isnumeric():
                    v = int(x)
                else:
                    v = ord(x) - 55

                for i in range(3, -1, -1):
                    if v & (1 << i):
                        test_line += '1'
                    else:
                        test_line += '0'

            code = []
            test_line = test_line.strip('0')
            while test_line:
                check = 0
                cnt = 0
                key = ''
                for i in range(len(test_line)):
                    cnt += 1
                    if test_line[i] == '1' and test_line[i+1] == '0':
                        if check:
                            key += str(cnt)
                            end = i+1
                            break
                        else:
                            check += 1
                    if test_line[i] != test_line[i+1]:
                        key += str(cnt)
                        cnt = 0

                test_line = test_line[end + 1:].strip('0')

                ok_cnt = 0
                while ok_cnt != 1:
                    c = 1
                    for keyV in D.keys():
                        if int(key) == c*int(keyV):
                            code += [D[keyV]]
                            ok_cnt = 1
                            break
                    c += 1

            sum1 = 0
            sum2 = 0
            for j in range(7):
                if j % 2:
                    sum2 += code[j]
                else:
                    sum1 += code[j]

            if (sum1 * 3 + sum2 + code[7]) % 10 == 0:
                if code not in used_code:
                    result += sum(code)
                used_code += [code]

    print(f'#{tc} {result}')