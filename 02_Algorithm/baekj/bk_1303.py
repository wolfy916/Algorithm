# 전쟁-전투

def stack_method(i, j, color):
    cnt = 1            # 병사수 카운트
    stack = [[i, j]]   # stack 시작 인덱스를 초기값으로 설정
    visited[i][j] = 1  # visited
    while stack:
        i, j = stack.pop()  # pop
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < M and 0 <= nj < N:  # 유효 인덱스 검사
                if area[ni][nj] == color and visited[ni][nj] != 1:  # 색깔, visited 검사
                    stack += [[ni, nj]]  # push
                    visited[ni][nj] = 1  # visited
                    cnt += 1
    return cnt**2  # 제곱값 리턴


N, M = map(int, input().split())
area = [list(input()) for _ in '_'*M]

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우 탐색 도구
visited = [[0]*N for _ in '_'*M]  # visited list
W = B = 0  # 최종 출력값
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:     # 방문한 곳이 아니라면
            if area[i][j] == 'W':  # 색깔에 따라 함수 호출
                W += stack_method(i, j, 'W')
            else:
                B += stack_method(i, j, 'B')

print(W, B)