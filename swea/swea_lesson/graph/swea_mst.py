# 10017. 5249. 최소 신장 트리

def find(a):
    while p[a] != a:
        a = p[a]
    return p[a]


def union(a, b):
    p[find(b)] = find(a)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V: V 마지막 정점, 0 ~ V, E: 총 간선수
    N = V + 1  # N: 정점 개수

    table = [0] * E  # 간선 정보를 받을 리스트
    for i in range(E):
        table[i] = list(map(int, input().split()))

    # 간선 정보를 최소 가중치 기준 오름차순으로 정렬
    table.sort(key=lambda x: x[2])

    # 최상단 조상노드가 같지 않은 노드를 연결한 간선을 선택
    p = list(range(N))
    cnt = total = 0  # cnt: 선택한 간선 수, total: MST 가중치 합
    for a, b, c in table:
        if find(a) != find(b):
            cnt += 1     # cnt
            union(a, b)  # union
            total += c   # 가중치 합산
            if cnt == N - 1:  # N-1: 신장트리가 되기 위한 간선 수
                break

    print(f'#{tc} {total}')