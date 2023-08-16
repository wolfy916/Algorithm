# 부동산 다툼
# 이진 트리 탐색 문제
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 이진 트리 역순 탐색 (자식 -> 부모)
def bottom_up(n, v):
    if n < 1: return v
    if tree[n]:
        v = n  # 마지막으로 마주치는 점유된 땅 번호 갱신
    return bottom_up(n // 2, v)

# [1] 입력 및 출력
N, Q = map(int, input().split())
tree = [False] * (N + 1)
for _ in range(Q):
    duck = int(input())
    print(bottom_up(duck, 0))
    if not tree[duck]:
        tree[duck] = True