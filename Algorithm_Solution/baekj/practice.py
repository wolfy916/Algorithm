# 최소 스패닝 트리
# 프림 알고리즘 풀이
# -> 대표적인 MST 알고리즘, 정점 중심의 접근법으로 간선이 많을 때 크루스칼보다 유리
import sys
from heapq import heappush, heappop

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [1] 데이터 입력 및 간선 기록
V, E = map(int, input().split())
adjL = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adjL[a].append((c, a, b))  # 양(무)방향 간선 표기
    adjL[b].append((c, b, a))  # ! 출발지도 포함시켜 기록하기 !

# [B] 프림 알고리즘
def prim(st):  # st = 시작 정점
    visited = [False] * (V + 1)  # 정점 기준의 visited
    visited[st] = True
    heap = sorted(adjL[st])  # 시작 정점의 인접 간선들을 가중치 기준 오름차순 정렬
    # mst = [] -> 이 문제에서는 mst 간선정보를 담을 필요가 없음
    tot_cost = 0
    while heap:
        cost, u, v = heappop(heap)
        if visited[v]: continue  # 이미 방문한 정점을 향한 간선이라면 버림
        visited[v] = True
        # mst.append((u, v))
        tot_cost += cost  # mst 가중치 누적
        for edge in adjL[v]:  # 현재 방문한 정점에 인접한 간선 탐색
            if visited[edge[2]]: continue
            heappush(heap, edge)
    return tot_cost

print(prim(1))