# # 도시분할계획
# # prim 4000ms
# import sys
# from heapq import heappop, heappush
#
# # [A] 입력 함수 초기화
# def input():
#     return sys.stdin.readline().rstrip('\n')
#
# # [B] prim
# def prim(N, adjL):
#     answer = 0
#     q = [(0, 1)]
#     maxV = cnt = 0
#     connected = [False] * (N + 1)
#     while q:
#         cost, v = heappop(q)
#         if connected[v]: continue
#         connected[v] = True
#         answer += cost
#         maxV = max(maxV, cost)  # 가장 비싼 간선 저장
#         cnt += 1
#         if cnt >= N - 2: break
#         for c, w in adjL[v]:
#             if connected[w]: continue
#             heappush(q, (c, w))
#
#     # 선택된 MST 간선중 가장 비용이 비싼 간선의 비용 빼기
#     return answer - maxV
#
# # [main]
# if __name__ == '__main__':
#     N, M = map(int, input().split())
#     adjL = [[] for _ in range(N + 1)]
#     for _ in range(M):
#         a, b, c = map(int, input().split())
#         adjL[a].append((c, b))
#         adjL[b].append((c, a))
#     print(prim(N, adjL))

# 도시분할계획
# kruskal 2500ms
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 부모 노드를 찾는 함수
def find(x, par):
    while x != par[x]:
        x = par[par[x]]
    return x

# [C] 부모노드를 병합하는 함수
def union(x, y, par):
    x = find(x, par)
    y = find(y, par)
    par[min(x, y)] = max(x, y)

# [D] MST 크루스칼
def kruskal(N, edges):
    edges.sort(key=lambda x: x[2])
    par = list(range(N + 1))
    cnt = answer = 0
    for a, b, c in edges:
        if cnt >= N - 2: break
        if find(a, par) != find(b, par):
            union(a, b, par)
            cnt += 1
            answer += c
    return answer

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print(kruskal(N, edges))