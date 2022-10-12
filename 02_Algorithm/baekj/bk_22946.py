# 원 이동하기 1
from sys import stdin
input = stdin.readline


def dfs(v, c, lst):  # v: 방문 노드, c: 간선 cnt, lst: 조상 노드들 기록
    global check
    visited[v] = 1
    if not chd[v]:  # 자식노드가 없으면
        check.append([c, set(lst)])
    else:
        for w in chd[v]:
            if not visited[w]:
                dfs(w, c+1, lst + [w])


N = int(input())
circles = [0] + [tuple(map(int, input().split())) for _ in '_'*N]

par = [0]*(N+1)
chd = [[] for _ in '_'*(N+1)]
for i in range(1, N+1):
    x, y, r = circles[i]
    min_r_gap, min_j = 10000, 0
    for j in range(1, N+1):
        if i != j:
            cx, cy, cr = circles[j]
            d = (cx-x)**2 + (cy-y)**2
            if cr > r:
                if d < (cr-r)**2 or d == 0:
                    if min_r_gap > abs(cr-r):
                        min_r_gap = abs(cr-r)
                        min_j = j
    par[i] = min_j
    chd[min_j].append(i)

top = 0  # 자식 노드가 2개 이상인 최상단 노드를 탐색
while len(chd[top]) == 1:
    top = chd[top][0]

check = []
visited = [0] * (N+1)
dfs(top, 0, [])
check.sort(reverse=True)  # 내림차순 정렬

cnt1, set1 = check[0][0], check[0][1]
for cnt2, set2 in check[1:]:
    if len(set1 & set2) == 0:  # 조상노드가 안겹치면 합산
        result = cnt1 + cnt2
        break

print(result)

