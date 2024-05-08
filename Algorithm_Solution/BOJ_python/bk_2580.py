# 스도쿠

# [A]
def dfs(zeros):
    lenV = len(zeros)
    if not lenV:
        for _ in range(9):
            print(*sudoku[_])
        exit()
    else:
        for x in range(lenV):
            i, j = zeros[x][0], zeros[x][1]
            for k in range(1, 10):
                if not sudoku[i][j] and possible(i, j, k):
                    sudoku[i][j] = k
                    dfs(zeros)
                    sudoku[i][j] = 0


# [B]
def possible(ii, jj, k):
    # 3 X 3
    box_i, box_j = ii//3, jj//3
    for i in range(box_i*3, box_i*3+3):
        for j in range(box_j*3, box_j*3+3):
            if sudoku[i][j] == k:
                return False
    # 열
    for i in range(9):
        if sudoku[i][jj] == k:
            return False
    # 행
    for j in range(9):
        if sudoku[ii][j] == k:
            return False

    return True


# [1]
sudoku = []
zeros = []
for i in range(9):
    line = list(map(int, input().split()))
    for j in range(9):
        if line[j] == 0:
            zeros.append((i, j))
    sudoku.append(line)
dfs(zeros)