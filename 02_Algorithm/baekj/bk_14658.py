# 하늘에서 별똥별이 빗발친다

from sys import stdin
# from collections import deque as dq

def input():
    return map(int, stdin.readline().rstrip("\n").split())

def isValid(x, y):
    if 0 <= x <= N and 0 <= y <= M:
        return True
    else:
        return False

def coordinates(a, b):
    xi, yi = a, b
    xj, yj = a + L, b + L
    cnt = K
    for xk in range(xi, xj+1):
        if 0 <= xk <= N:
            if xk == xi or xk == xj:
                for yk in range(yi, yj+1):
                    # if 0 <= yk <= M and (xk, yk) not in used:
                    if 0 <= yk <= M:
                        cnt = min(cnt, leftBottom(xk, yk))
                        # used.append((xk, yk))
            else:
                for yk in [yi, yj]:
                    # if 0 <= yk <= M and (xk, yk) not in used:
                    if 0 <= yk <= M:
                        cnt = min(cnt, leftBottom(xk, yk))
                        # used.append((xk, yk))
    return cnt

def leftBottom(a, b):
    xi, yi = a - L, b - L
    xj, yj = a, b
    return calculate(xi, yi, xj, yj)

def calculate(xi, yi, xj, yj):
    cnt = K
    if isValid(xi, yi):
        for x, y in stars:
            if xi <= x <= xj and yi <= y <= yj:
                cnt -= 1
    return cnt

N, M, L, K = input()
stars = [list(input()) for _ in '_'*K]
result = K
# used = dq([])
for x, y in stars:
    result = min(result, coordinates(x, y))
print(result)