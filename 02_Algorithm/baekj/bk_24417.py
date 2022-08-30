# 알고리즘 수업 - 피보나치 수 2
import sys

n = int(sys.stdin.readline())
f = [1, 1]
for i in range(2, n):  # DP를 이용한 리스트 f의 마지막 원소의 값 = 재귀 횟수
    f += [f[-1] + f[-2]]
    f.pop(0)
    if f[-1] > 1000000007:
        f[-1] -= 1000000007
print(f[-1], n-2)