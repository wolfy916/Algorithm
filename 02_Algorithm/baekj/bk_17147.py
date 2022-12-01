# 연구소 2

# input, 바이러스 위치와 벽 인덱스를 리스트에 저장
N, M = map(int, input().split())
lab = []
wall = []
possible = []
for i in range(N):
    line = list(map(int, input().split()))
    lab.append(line)
    for j in range(N):
        if line[j] == 2:
            possible.append((i, j))  # 바이러스 놓을 수 있는 위치 인덱스 모으기
        elif line[j] == 1:
            wall.append((i, j))  # 벽 놓을 수 있는 위치 인덱스 모으기

# bfs
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(comb):
    test_lab = [[0]*N for _ in '_'*N]
    for wi, wj in wall:  # 벽 세우기
        test_lab[wi][wj] = 1
    q = []
    for i, j in comb:  # 바이러스 놓기
        q.append((i, j))
        test_lab[i][j] = 2
    while q:
        vi, vj = q.pop(0)
        for di, dj in delta:
            ni, nj = vi+di, vj+dj
            if 0 <= ni < N and 0 <= nj < N and not test_lab[ni][nj]:
                test_lab[ni][nj] = test_lab[vi][vj] + 1
                q.append((ni, nj))

    # 0 하나라도 발견하면 닥 -1 리턴
    for i in range(N):
        if 0 in test_lab[i]:
            return -1

    return max(map(max, test_lab)) - 2  # 0 발견 못했으니 리턴

from itertools import combinations as cb
combs = list(cb(possible, M))  # 조합 생성

minV = 99999  # 대충 큰 값
for comb in combs:  # 조합 하나씩 꺼내서 bfs로 돌림
    value = bfs(comb)
    if value == -1:
        continue
    elif minV > value:
        minV = value

if minV == 99999:  # 그대로 큰 값이면 -1 ㄱㄱ
    minV = -1

print(minV)
