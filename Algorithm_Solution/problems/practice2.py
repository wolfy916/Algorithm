def solution(board):
    turn = ['O', 'X']
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    test_board = [['.' for _ in range(3)] for _ in range(3)]

    def dfs(cur_cnt, total_cnt, player, is_end):
        if cur_cnt == total_cnt or is_end:
            for i in range(3):
                for j in range(3):
                    if board[i][j] != test_board[i][j]:
                        return False
            return True
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] != '.' and test_board[i][j] == '.':
                        test_board[i][j] = turn[player]
                        if j == 1:
                            if test_board[i][j - 1] == test_board[i][j + 1] == turn[player]:
                                is_end = True
                        if i == 1:
                            if test_board[i - 1][j] == test_board[i + 1][j] == turn[player]:
                                is_end = True
                        for di, dj in delta:
                            ni, nj = i + di, j + dj
                            mi, mj = i + 2 * di, j + 2 * dj
                            if 0 <= mi < 3 and 0 <= mj < 3:
                                if test_board[ni][nj] == test_board[mi][mj] == turn[player]:
                                    is_end = True

                        if dfs(cur_cnt + 1, total_cnt, (player + 1) % 2, is_end):
                            return True
                        test_board[i][j] = '.'
                        is_end = False
            return False

    total_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != '.':
                total_cnt += 1
    return 1 if dfs(0, total_cnt, 0, False) else 0

board = ["OOO", "...", "XXX"]
print(solution(board))