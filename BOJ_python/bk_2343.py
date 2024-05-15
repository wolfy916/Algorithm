# 기타 레슨
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

N, M = map(int, input().split())
videos = list(map(int, input().split()))

def check(m):
    sumV = 0
    cnt = 0
    for v in videos:
        if v > m: return False
        if sumV + v <= m:
            sumV += v
        else:
            cnt += 1
            sumV = v
        if cnt > M: return False
    if cnt > M - 1: return False
    return True

left, right = 1, int(1e9)
while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1

print(left)