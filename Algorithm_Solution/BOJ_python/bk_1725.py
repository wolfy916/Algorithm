'''
히스토그램 - 백준 플레5
분류 : 스택
'''
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == '__main__':
    N = int(input())
    heights = [int(input()) for _ in range(N)]

    answer = 0
    stack = []
    for i in range(N):
        idx = i
        while stack and stack[-1][1] > heights[i]:
            idx, h = stack.pop()
            answer = max(answer, (i - idx) * h)
        stack.append((idx, heights[i]))

    while stack:
        idx, h = stack.pop()
        answer = max(answer, (N - idx) * h)

    print(answer)