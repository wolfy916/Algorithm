"""
최소 회의실 개수 - 백준(골드5)
분류 : 우선순위 큐
"""
import sys
from heapq import heappush, heappop

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    N = int(input())
    times = sorted([tuple(map(int, input().split())) for _ in range(N)])
    rooms = []
    for s, e in times:
        if rooms and rooms[0] <= s:
            heappop(rooms)
        heappush(rooms, e)
    print(len(rooms))
