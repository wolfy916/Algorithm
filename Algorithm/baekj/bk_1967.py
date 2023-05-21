# 트리의 지름
'''
메모리 초과 뎀프시롤 얻어맞고, adjM이 아니라는 것을 깨달음
시간초과 몇 대 맞고, 리프 노드로만 계산해야 된다는 것을 깨달음
python으로 제출하면 시간초과인 코드입니다.
'''
from sys import setrecursionlimit

setrecursionlimit(50000)

n = int(input())
adjL = [[] for _ in '_' * (n + 1)]
values = [0] * (n + 1)  # 가중치 담을 리스트

for _ in range(n - 1):
    par, chd, value = map(int, input().split())
    adjL[par].append(chd)  # 양방향 간선
    adjL[chd].append(par)  #
    values[chd] = value  # 자식노드 번호를 인덱스로 가중치 할당


# [A] 출발 노드부터 가중치를 합산하며 재귀하는 dfs
def dfs(s, v):  # s: 방문 노드, v: 가중치 합산
    global maxV
    visited[s] = 1
    check = 1  # 리프노드 check 하기 위한 값
    for w in adjL[s]:
        if not visited[w]:
            if s < w:  # 노드 번호가 크다면 s가 부모이므로 가중치에 values[w]를 더 함
                dfs(w, v + values[w])
                check = 0
            else:  # 노드 번호가 작다면 w가 부모이므로 가중치에 values[s]를 더 함
                dfs(w, v + values[s])
                check = 0

    # [A-1] 리프노드라면 -> 재귀하지 않았으므로 -> check = 1일 것임
    if check:
        if maxV < v:  # maxV 갱신 시도
            maxV = v


# [1] 리프 노드로만 dfs 출발
maxV = 0
for i in range(1, n + 1):
    if len(adjL[i]) == 1:  # 연결된 노드가 1개뿐이라면 리프 노드
        visited = [0] * (n + 1)
        dfs(i, 0)
print(maxV)