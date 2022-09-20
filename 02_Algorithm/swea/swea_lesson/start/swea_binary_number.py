# 이진수(제출용)

for tc in range(1, int(input()) + 1):
    N, number = input().split()
    N = int(N)

    line = []
    for a in number:
        if a.isnumeric():
            line += [int(a)]
        else:
            line += [ord(a) - 55]

    result = ''
    for b in line:
        for i in range(3, -1, -1):
            if b & (1 << i):
                result += '1'
            else:
                result += '0'

    print(f'#{tc} {result}')