# Z
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 재귀 함수
def z(n, si, sj, r, c, order):
    if n == 0:
        print(order)
        return
    area = 4 ** (n - 1)  # 4구역으로 나누었을때 한 구역의 칸 개수
    vi, vj = si, sj
    if si + 2 ** (n - 1) <= r:
        vi += 2 ** (n - 1)
        order += 2 * area
    if sj + 2 ** (n - 1) <= c:
        vj += 2 ** (n - 1)
        order += area
    z(n - 1, vi, vj, r, c, order)

# [main]
if __name__ == '__main__':
    N, r, c = map(int, input().split())
    z(N, 0, 0, r, c, 0)