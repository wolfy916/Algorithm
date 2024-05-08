# 오큰수
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution(N, A):
    stack = [A[-1]]
    result = []
    for i in range(N-1, -1, -1):
        while stack and A[i] >= stack[-1]:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(A[i])
    return reversed(result)

# [main]
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(*solution(N, A))