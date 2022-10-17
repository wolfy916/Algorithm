# DSLR
from sys import stdin
from collections import deque
input = stdin.readline
DSLR = ['D', 'S', 'L', 'R']


def cal(n, m):
    if m == 0:
        n = (n * 2) % 10000
    elif m == 1:
        n -= 1
        if n < 0:
            n = 9999
    else:
        n = str(n)
        n = '0'*(4-len(n)) + n
        if m == 2:
            n = n[1:] + n[:1]
        elif m == 3:
            n = n[3:] + n[:3]
        if n == '0000':
            n = 0
        else:
            n = int(n.lstrip('0'))
    return n


def bfs(s, e):
    calculated = [0] * 10001
    q = deque([(s, [])])
    calculated[s] = 1
    while q:
        v, method = q.popleft()
        if v == e:
            return method
        else:
            for i in range(4):
                w = cal(v, i)
                if not calculated[w]:
                    calculated[w] = 1
                    q.append((w, method + [i]))


T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    for m in bfs(A, B):
        print(DSLR[m], end='')
    print()