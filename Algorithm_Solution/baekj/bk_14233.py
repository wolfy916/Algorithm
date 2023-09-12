# 악덕 사장
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution(N, A):
    A.sort()
    answer = int(1e9)
    for i in range(N):
        answer = min(answer, A[i] // (i + 1))
    return answer

# [main]
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))