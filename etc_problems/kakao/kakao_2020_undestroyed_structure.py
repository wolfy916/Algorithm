# 파괴되지 않은 건물

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

def solution(board, skill):
    n, m = len(board), len(board[0])
    answer = 0
    temp_board = [[0] * (m + 1) for _ in '_' * (n + 1)]
    for subject, r1, c1, r2, c2, degree in skill:
        temp = -1 * degree if subject == 1 else degree
        temp_board[r1][c1] += temp
        temp_board[r1][c2 + 1] += -temp
        temp_board[r2 + 1][c1] += -temp
        temp_board[r2 + 1][c2 + 1] += temp

    for i in range(n + 1):
        for j in range(m):
            temp_board[i][j + 1] += temp_board[i][j]

    for i in range(n):
        for j in range(m + 1):
            temp_board[i + 1][j] += temp_board[i][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += temp_board[i][j]
            # if board[i][j] + temp_board[i][j] > 0:
            #     answer += 1
    return board

print(solution(board, skill))