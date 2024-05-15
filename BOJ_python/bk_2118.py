# 두 개의 탑
from sys import stdin

# [A] 입력 초기화
def input():
    return stdin.readline().rstrip('\n')

# [1] 거리 표기 및 누적합 진행
N = int(input())
points = [0] * N
for i in range(N):
    points[i] = int(input())
for i in range(N - 1):
    points[i + 1] += points[i]

# [2] 특정 구간의 (구간합)과 (sumV - 구간합)의 최솟값을 찾아 maxV를 갱신
maxV = 0
sumV = points[-1]
for p1 in range(N):
    for p2 in range(p1 + 1, N + 1):
        a = points[p2 - 1] if p1 == 0 else points[p2 - 1] - points[p1]
        b = sumV - a
        minV = min(a, b)
        maxV = max(maxV, minV)

print(maxV)

"""
[2]에서 a, b = 3, 7이 나왔다면 7, 3도 나옴
사실상, 같은 지점에 거리에 대해 2번씩 계산하는 비효율적인 코드
"""