# 카드2
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution(N):
    nums = dq(list(range(1, N + 1)))
    i = 1
    while len(nums) > 1:
        if i % 2:
            nums.popleft()
        else:
            nums.append(nums.popleft())
        i += 1
    return nums[0]

# [main]
if __name__ == '__main__':
    N = int(input())
    print(solution(N))