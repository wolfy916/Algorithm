"""
행성 터널 - 백준 플레5
분류 : ?
"""
import sys
from heapq import heappop, heappush

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == '__main__':
    N = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(N)]

    coords.sort(key=lambda x: [x[0], x[1], x[2]])
    print(coords)

    for i in range(1, N):
        tmp = [abs(coords[0][j] - coords[i][j]) for j in range(3)]
        print(min(tmp), end=" ")