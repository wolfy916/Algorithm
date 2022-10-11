# 원 이동하기 1
from sys import stdin
input = stdin.readline

N = int(input())
chd = [[] for _ in '_'*(N+1)]
par = [0]*(N+1)
circles = [0] + [tuple(map(int, input().split())) for _ in '_'*N]
for i in range(1, N+1):
    x, y, r = circles[i]
    min_r_gap = 10000
    min_j = 0
    for j in range(1, N+1):
        cx, cy, cr = circles[j]
        if i == j:
            continue
        d = (cx-x)**2 + (cy-y)**2
        if cr > r:
            if d < (cr-r)**2 or d == 0:
                if min_r_gap > abs(cr-r):
                    min_r_gap = abs(cr-r)
                    min_j = j
    par[i] = min_j
    chd[min_j].append(i)

print(par)
print(chd)

check = []
for i in range(1, N+1):
    if not chd[i]:
        cnt = 0
        num = i
        while par[num] != 0:
            num = par[num]
            cnt += 1
        check.append(cnt)
check.sort(reverse=True)
print(check)
print(check[0] + check[1])