# 알파벳 dfs 재귀
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# dfs
def dfs(vi, vj, k):
    global maxV

    # 최대값 갱신
    if maxV < k:
        maxV = k

    # visited, alpha(아스키코드 활용)
    visited[vi][vj] = 1
    alpha[ord(board[vi][vj])-64] = 1

    # 방문한 위치에서 delta
    for di, dj in delta:
        ni, nj = vi+di, vj+dj
        v = board[ni][nj]
        # 해당 위치가 0이 아니고, 방문하지 않은 위치고, 방문하지 않은 알파벳이라면
        if v and not visited[ni][nj] and not alpha[ord(v)-64]:
            dfs(ni, nj, k+1)  # dfs
            visited[ni][nj] = 0   # return 하고 backtracking
            alpha[ord(v)-64] = 0  #

# 입력
N, M = map(int, input().split())  # 1 <= R, C <= 20
board = [[0]*(M+2)] + [[0] + list(input()) + [0] for _ in '_'*N] + [[0]*(M+2)]

# 격자 visited, 알파벳 visited, 최종 출력할 maxV
visited = [[0]*(M+2) for _ in '_'*(N+2)]
alpha = [0]*27
maxV = 0
dfs(1, 1, 1)
print(maxV)

# # 알파벳 stack
# delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# N, M = map(int, input().split())
# board = [[0] * (M + 2)] + [[0] + list(input()) + [0] for _ in '_' * N] + [[0] * (M + 2)]
#
# visited = [[0]*(M+2) for _ in '_'*(N+2)]
# maxV = 0
# stack = [(1, 1, 1, board[1][1])]  # i, j, 알파벳 개수, 선택한 알파벳
#
# # dfs -> stack
# while stack and maxV != 26:
#     vi, vj, k, string = stack.pop()
#
#     if maxV < k:
#         maxV = k
#
#     for di, dj in delta:
#         ni, nj = vi + di, vj + dj
#         v = board[ni][nj]
#
#         # 해당 위치가 알파벳이고, 그 알파벳이 내가 선택한 string 중에 없으면
#         if v and v not in string:
#             new_string = string + board[ni][nj]  # 알파벳 추가하여 new_string 생성
#             if visited[ni][nj] != new_string:    # 생성된 new_string 이 기존의 것이아니라면
#                 visited[ni][nj] = new_string     # visited에 갱신하고
#                 stack.append((ni, nj, k + 1, new_string))  # 방문
# print(maxV)