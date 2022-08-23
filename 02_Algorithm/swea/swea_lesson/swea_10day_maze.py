# #  재귀적방법으로 풀기
# def find_end(i, j, N):  # 도착여부를 확인하는 재귀함수, 중복방문 불필요
#     if maze[i][j] == 3:
#         return 1
#     else:
#         maze[i][j] = 1  # 중복방지(방문한 곳을 1로 바꿈)
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:  # 벽이 아니면.. (통로 또는 도착지)
#                 if find_end(ni, nj, N) == 1:
#                     return 1  # 진행방향에서 도차기를 찾은 경우
#         return 0  # 도착지를 찾지 못하고, 리턴하는 경우

#  stack으로 풀기
def find_end(i, j, N):
    stack = [(i, j)]
    visited = [[0] * N for _ in '_' * N]
    visited[i][j] = 1
    while stack:
        i, j = stack.pop()
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append((ni, nj))  # 방문한 칸 대신 갈 수 있는 칸들을 스택에 push
                visited[ni][nj] = 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in '_'*N]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i = i
                start_j = j
                break

    print(f'#{tc} {find_end(start_i, start_j, N)}')
