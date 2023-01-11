# Yes or yes

# 기본 bfs
N, M = map(int, input().split())
adjL = [[] for _ in '_'*(N+1)]  # 인접리스트
for _ in '_'*M:
    u, v = map(int, input().split())
    adjL[u].append(v)  # 단방향 간선 표기
S = int(input())
fans = list(map(int, input().split()))
result = 0
# 시작점에 fan이 있으면 바로 종료
if 1 not in fans:
    q = [1]
    while q:
        v = q.pop(0)
        if not adjL[v]:
            result = 1  # fan 안만나고 루트 노드에 도달하는 방법이 있음
            break
        else:
            for w in adjL[v]:
                # fan이 없는 노드라면 방문
                if w not in fans:
                    q.append(w)
if result:
    print('yes')
else:
    print('Yes')