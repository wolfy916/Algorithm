'''
월향, 비상 - 백준 실버2
분류 : 그리디, 정렬
'''

import sys

def input():
    return sys.stdin.readline().rstrip('\n')

def solution():
    quality = 0
    nxt = 0
    for i in range(M):
        t, q = conditions[i]
        for j in range(nxt, N):
            if quality >= q: break
            quality += ability[j] + t
            nxt = j + 1

        if quality < q: return -1

    for k in range(nxt, N):
        quality += ability[k] + t

    return quality

if __name__ == '__main__':
    N, M = map(int, input().split())
    ability = sorted(list(map(int, input().split())), reverse=True)
    conditions = [tuple(map(int, input().split())) for _ in range(M)]

    print(solution())