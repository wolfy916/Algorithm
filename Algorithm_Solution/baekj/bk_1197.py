import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 부모 노드를 찾는 find 함수
def find(n):
    while parent[n] != n:
        n = parent[n]
    return n

# [C] union 함수 설정. a와 b 집합을 합쳐주는 역할을 한다.
def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a, b)] = min(a, b)


# [1] 간선과 가중치 정보들을 edges에 저장하고, 가중치 순으로 정렬
V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]
edges.sort(key = lambda x:x[2])

# [2] 가중치가 낮은 순으로 노드를 연결한다.
# find(A)와 find(B)가 같다면 이미 연결된 노드이므로 무시한다.
tot_cost = 0
parent = list(range(V + 1))
for A, B, C in edges:
    if find(A) != find(B):
        union(A, B)
        tot_cost += C

print(tot_cost)