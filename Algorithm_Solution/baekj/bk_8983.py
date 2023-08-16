# 사냥꾼
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

def can_hunt(hx, a, b):
    return abs(hx - a) + b <= L

M, N, L = map(int, input().split())
hunt = list(map(int, input().split()))
hunt.sort()
answer = 0
for _ in range(N):
    x, y = map(int, input().split())
    left, right = 0, len(hunt)
    while left < right:
        mid = (left + right) // 2
        if can_hunt(hunt[mid], x, y):
            answer += 1
            break
        if hunt[mid] >= x:
            right = mid
        else:
            left = mid + 1
print(answer)