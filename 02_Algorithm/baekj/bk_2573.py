# 빙산

# 빙산이 몇 개의 덩어리로 이루어져있는지 확인하는 check 함수
# stack -> dfs
def check():
    visited = [[0] * M for _ in '_' * N]
    cnt = 0  # 빙산 덩어리 개수
    for i in range(1, N):
        for j in range(1, M):
            if area[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = cnt
                stack = [(i, j)]
                while stack:
                    vi, vj = stack.pop()
                    for di, dj in delta:
                        wi, wj = vi+di, vj+dj
                        if area[wi][wj] and not visited[wi][wj]:
                            visited[wi][wj] = cnt
                            stack.append((wi, wj))

            # 빙산이 두 덩어리라면 종료
            if cnt == 2:
                return cnt

    # 탐색 종료시 몇 개의 덩어리인지 return
    return cnt


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in '_'*N]

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
year = 0  # 최종 출력값
while True:
    # 빙하 개수에 따른 종료 조건
    glacial_mass = check()
    if glacial_mass == 2:  # 2개인 경우
        break
    elif glacial_mass == 0:  # 모두 녹은 경우
        year = 0
        break

    year += 1

    melt = []  # 각 빙하의 i,j와 녹는 양 m을 담아놓을 리스트
    for i in range(1, N):
        for j in range(1, M):
            if area[i][j]:
                m = 0
                for di, dj in delta:
                    ni, nj = i+di, j+dj
                    if not area[ni][nj]:
                        m += 1
                melt.append((i, j, m))

    # 빙산 녹이기
    for i, j, m in melt:
        area[i][j] -= m
        if area[i][j] < 0:  # 음수는 나올수 없으므로 0
            area[i][j] = 0

print(year)