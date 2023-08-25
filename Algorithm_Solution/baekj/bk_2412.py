# 암벽등반
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 이동할 수 있는 거리인지 확인하는 함수
def is_possible(a, b, x, y):
    return abs(a - x) <= 2 and abs(b - y) <= 2

# [C] 이동 가능한 좌표들를 탐색 후, 이동하는 함수
def move(T, ref, floor):
    ref[(0, 0)] = 0
    q = dq([(0, 0, 0)])
    while q:
        a, b, cnt = q.popleft()
        if b == T: return cnt
        for nxt in range(b - 2, b + 3):
            if nxt < 0 or nxt >= T+1: continue
            for x, y in floor[nxt]:
                if not is_possible(a, b, x, y): continue
                if ref[(x, y)] <= cnt + 1: continue
                ref[(x, y)] = cnt + 1
                q.append((x, y, cnt + 1))
    return -1

# [D] 메인 로직 함수
def solution(_, T, coords):
    INF = float('inf')
    floor = [[] for _ in range(T + 1)]
    for x, y in coords:
        floor[y].append((x, y))
    floor[0].append((0, 0))
    ref = {(x, y): INF for x, y in coords}
    return move(T, ref, floor)

# [main]
if __name__ == '__main__':
    n, T = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, T, coords))