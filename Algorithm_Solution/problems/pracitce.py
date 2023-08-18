# 풀이 1. 완전 탐색
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

TC = int(input())
for _ in range(TC):
    M, N, x, y = map(int, input().split())
    ans = 0
    a = b = 0
    print(a, b, ans)
    while a != x or b != y:
        a = (a + 1) % (M + 1)  # 1씩 더하는 귀요미
        if a == 0: a = 1
        b = (b + 1) % (N + 1)  #
        if b == 0: b = 1
        ans += 1
        if b == y:
            print(a, b, ans)
        if (a, b) == (M, N):
            if (x, y) != (M, N):
                ans = -1
            break
    print(ans)