# 집합의 표현
import sys
input = sys.stdin.readline


def find_set(x):  # 최상단 조상 노드를 반환
    if x != par[x]:
        par[x] = find_set(par[x])
    return par[x]


def link(x, y):  # 노드 깊이를 비교하여 조상 노드 할당
    if rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def union(x, y):  # 두 노드의 최상단 노드끼리 비교
    link(find_set(x), find_set(y))


N, M = map(int, input().split())
par = list(range(N+1))
rank = [0] * (N+1)
for _ in '_'*M:
    c, a, b = map(int, input().split())
    if c:
        if find_set(a) != find_set(b):
            print('NO')
        else:
            print('YES')
    else:
        union(a, b)