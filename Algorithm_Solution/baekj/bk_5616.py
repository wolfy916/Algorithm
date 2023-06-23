# 로드샵
import sys
sys.setrecursionlimit(100000)

def fa(n):
    return 1 if n < 2 else n * fa(n-1)

def nCr(n, r):
    return fa(n) // (fa(r) * fa(n-r))

n, m, r = map(int, input().split())
if m != 0 and n * m > r:
    print(0)
else:
    print(nCr(n + r - n * m - 1, r - n * m) if m != 0 else nCr(n + r - 1, r))