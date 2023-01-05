# 로봇 청소기

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# [A] start -> end 까지의 최단 거리를 반환하는 bfs 함수
def distance_bfs(s:tuple, e:tuple):
    visited = [[0]*w for _ in '_'*h]
    q = [s]
    visited[s[0]][s[1]] = 1
    while q:
        vi, vj = q.pop(0)
        # [A-1] 종료 조건 : end 인덱스의 도착
        if (vi, vj) == e:
            return visited[vi][vj]  # 최단거리 반환하며 함수 종료

        # [A-2] visited에 거리 기록, 벽이 아닌 곳 방문
        for di, dj in delta:
            ni, nj = vi+di, vj+dj
            if 0 <= ni < h and 0 <= nj < w:  # 유효 인덱스 검사
                if not visited[ni][nj] and area[ni][nj] != 'x':
                    visited[ni][nj] = visited[vi][vj] + 1
                    q.append((ni, nj))
    # [A-3] start에서 end로 갈 수 있는 경로가 없음
    return 0

# [B] 로봇이 청소를 완료할 수 있는 모든 경로를 탐색하는 dfs 함수
def path_dfs(v, cnt, value):
    global minV, lenV  # 최종 출력할 minV, 더러운 곳의 갯수
    
    # [B-1] 현재 minV보다 가중치의 합이 커지면 가지치기
    if value > minV:
        return

    # [B-2] 모든 청소를 완료했을때 minV 갱신 시도
    if cnt == lenV:
        minV = min(minV, value)
    else:
        for w in range(lenV):
            # [B-3] 연결이되있고, 방문하지 않은 곳일 때
            if graph[v][w] and not visited_dfs[w]:
                visited_dfs[w] = 1  #
                path_dfs(w, cnt+1, value+graph[v][w])
                visited_dfs[w] = 0  # backtracking

while True:
    w, h = map(int, input().split())
    if not w:  # input 종료지점
        break
    area = [list(input()) for _ in '_'*h]

    # [1] 로봇 시작지점 인덱스 할당과 더러운 곳의 인덱스 리스트화
    dirts = []
    for i in range(h):
        for j in range(w):
            if area[i][j] == '*':
                dirts.append((i, j))
            elif area[i][j] == 'o':
                si, sj = i, j
    dirts = [(si, sj)] + dirts  # 맨 앞에 로봇 시작지점 추가

    # [2] 각 구역을 노드화 하여 거리를 간선의 가중치화
    lenV = len(dirts)
    INF = 1000000
    graph = [[0]*lenV for _ in '_'*lenV]
    for i in range(lenV):
        for j in range(lenV):
            if i != j and not graph[i][j]:
                graph[i][j] = graph[j][i] = distance_bfs(dirts[i], dirts[j])

    # [3] [2]에서 만든 그래프로 dfs 실행
    minV = INF
    visited_dfs = [0] * lenV
    visited_dfs[0] = 1
    path_dfs(0, 1, 0)
    if minV == INF:
        print(-1)
    else:
        print(minV - lenV + 1)