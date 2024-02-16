'''
카드 놓기 - 백준 실버 3
분류 : 시뮬레이션
'''
import sys
from collections import deque as dq

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력 및 초기화
    N = int(input())
    nums = tuple(map(int, input().split()))

    # [2] 시뮬레이션
    tmp1 = list(range(N, 0, -1))
    tmp2 = dq([])
    for i in range(N - 1, -1, -1):
        card = tmp1.pop()
        if nums[i] < 2:
            tmp2.insert(0, card)
        elif nums[i] < 3:
            tmp2.insert(1, card)
        else:
            tmp2.append(card)

    print(*tmp2)
