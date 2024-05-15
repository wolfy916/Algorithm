# 카드 합체 놀이
import sys
from heapq import heapify, heappop, heappush

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution(_, m, a):
    heapify(a)
    for _ in range(m):
        a1, a2 = heappop(a), heappop(a)
        heappush(a, a1 + a2)
        heappush(a, a1 + a2)
    return sum(a)

# [main]
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solution(n, m, a))