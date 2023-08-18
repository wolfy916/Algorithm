# 로마 숫자
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [1] 데이터 입력 및 초기화
num1 = input()
num2 = input()
ref = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

# [B] 로마 숫자 -> 아라비안 숫자 변환 함수
def trans_to_num(num):
    sumV, prev = 0, 10000
    for n in num:
        for k, v in ref.items():
            if n != v: continue
            sumV += k
            if prev < k: sumV += -2 * prev
            prev = k
    return sumV

# [2] 입력 받은 두 숫자를 더함
num1 = trans_to_num(num1)
num2 = trans_to_num(num2)
sumV = num1 + num2

# [C] 아라비안 숫자 -> 로마 숫자 변환 함수
def trans_to_Rome(num):
    ret = ''
    while num > 0:
        for k in sorted(ref.keys(), reverse=True):
            if num < k: continue
            if str(k)[0] == '5' and num // (k // 5) == 9: continue
            v = num // k
            if v == 4:
                ret += ref[k] + ref[k * 5]
            elif v == 9:
                ret += ref[k] + ref[k * 10]
            else:
                ret += ref[k] * v
            num %= k
            break
    return ret

# [3] 출력
print(sumV)
print(trans_to_Rome(sumV))