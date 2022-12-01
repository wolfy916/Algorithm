# 치즈

# [A] 인접한 0을 모두 -1로 바꿈 (외부 공기화시킴)
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def outside(i, j):
    q = [(i, j)]
    cheese[i][j] = -1
    while q:
        vi, vj = q.pop(0)
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if 0 <= ni < N and 0 <= nj < M and not cheese[ni][nj]:
                cheese[ni][nj] = -1
                q.append((ni, nj))

# [1] Input
N, M = map(int, input().split())
cheese = []
cheese_num = 0
for i in range(N):
    line = list(map(int, input().split()))
    cheese_num += line.count(1)  # 치즈 갯수 세기
    cheese.append(line)

# [2] 외부 공기를 모두 0 -> -1로 값 재할당
outside(0, 0)

# [3] 치즈 갯수가 0이 될때까지 반복
time = 0
while cheese_num:
    melt = []
    # [3-1] 외부공기(-1)와 2면 이상 인접한 치즈를 append
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                air_cnt = 0  # 인접 외부공기 cnt
                for di, dj in delta:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < M and cheese[ni][nj] == -1:
                        air_cnt += 1
                if air_cnt >= 2:
                    melt.append((i, j))
    # [3-2] 치즈를 녹이면서 외부공기를 유입시킴
    for vi, vj in melt:
        cheese_num -= 1
        outside(vi, vj)
    time += 1  # 시간 cnt

print(time)