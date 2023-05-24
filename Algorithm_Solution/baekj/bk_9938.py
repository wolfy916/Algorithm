# 방 청소
import sys
input = sys.stdin.readline

def is_empty(idx, n):
    return cabinets[alcohols[idx][n]]

def alcohol_in(idx, n):
    cabinets[alcohols[idx][n]].append(idx)

def alcohol_out(idx, n):
    return cabinets[alcohols[idx][n]].pop()

def is_possible(idx, n):
    cabinet = is_empty(idx, 1 - n)
    if not cabinet:
        return True
    else:
        alcohol_in_cabinet = cabinet[0]



N, L = map(int, input().rstrip('\n').split())
alcohols = [0, (tuple(map(int, input().rstrip('\n').split())) for _ in range(N))]
cabinets = [[] for _ in range(1, L + 1)]

for i in range()