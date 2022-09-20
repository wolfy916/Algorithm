# 이진수2

for tc in range(1, int(input()) + 1):
    num = float(input()) * (2 ** 12)
    int_num = int(num)
    result = ''
    if int_num == num:
        for i in range(11, -1, -1):
            if int_num & (1 << i): result += '1'
            else: result += '0'
    else:
        result = 'overflow'
    print(f'#{tc} {result.rstrip("0")}')