# 전화번호 목록
import sys
from collections import Counter

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

TC = int(input())
for _ in range(TC):
    # [1] 데이터 입력 및 초기화
    N = int(input())
    nums = [input() for _ in range(N)]
    counter = Counter(nums)  # 카운터 dict
    flag = True

    # [2] 각 넘버를 앞자리 부터 하나씩 추가해 가며 key 존재 유무 확인
    for num in nums:
        tmp = ''
        for n in num:
            tmp += n
            if tmp != num and counter.get(tmp):
                print('NO')
                flag = False
                break
        if not flag: break
    if not flag: continue
    print('YES')