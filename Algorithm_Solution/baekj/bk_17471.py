# 게리맨더링
import sys
from collections import deque as dq
from itertools import combinations as cb

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [1] 데이터 입력 및 간선 기록
N = int(input())
area = [0] + list(map(int, input().split()))
adjL = [[] for _ in range(N + 1)]
for n in range(1, N + 1):
    num, *lst = map(int, input().split())
    for i in range(num):
        adjL[n].append(lst[i])

# [B] 조합에 대한 유효성 검사를 진행하는 bfs 함수
def bfs(comb):

    # [B-1] 첫번째 그룹이 모두 연결되어 있는지 확인
    visited = [0] * (N + 1)
    visited[0] = -1
    for n in comb:
        visited[n] = 1
    q = dq([visited.index(0)])
    visited[q[-1]] = 2
    while q:
        v = q.popleft()
        for w in adjL[v]:
            if visited[w] == 0:
                visited[w] = 2
                q.append(w)

    if visited.count(0) > 0: return False

    # [B-2] 두번째 그룹이 모두 연결되어 있는지 확인
    q = dq([visited.index(1)])
    visited[q[-1]] = 3
    while q:
        v = q.popleft()
        for w in adjL[v]:
            if visited[w] == 1:
                visited[w] = 3
                q.append(w)

    if visited.count(1) > 0: return False

    return True

# [2] 구역을 나누는 조합의 유효성을 검사하고, answer 갱신
answer = 1001
tot_sumV = sum(area)
for i in range(1, N // 2 + 1):
    combs = cb(range(1, N + 1), i)
    for comb in combs:
        if bfs(comb):
            sumV = sum(map(lambda x: area[x], comb))
            answer = min(answer, abs(tot_sumV - 2 * sumV))
print(answer if answer != 1001 else -1)