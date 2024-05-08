# 줄 세우기
import sys
sys.setrecursionlimit(32001)

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] v보다 작은 친구가 있으면 작은 친구 먼저 출력
def new_print(v):
    if adjL[v]:
        for w in adjL[v]:
            if printed[w]: continue
            new_print(w)
    if printed[v]: return
    printed[v] = True
    print(v, end=' ')

# [C] 줄 세워 출력하기
def line_up(N, orders):
    global adjL, printed

    # 단방향 간선 역표기 b -> a
    adjL = [[] for _ in range(N + 1)]
    for a, b in orders:
        adjL[b].append(a)

    # 출력 여부 배열과 출력 함수 실행
    printed = [False] * (N + 1)
    for n in range(1, N + 1):
        if printed[n]: continue
        new_print(n)

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    orders = [tuple(map(int, input().split())) for _ in range(M)]
    line_up(N, orders)