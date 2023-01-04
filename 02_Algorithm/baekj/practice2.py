# 스도쿠

sudoku = []
for i in range(9):
    line = list(map(int, input().split()))

flag = 1
while flag:
    flag = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                flag = 1
                if sudoku[i].count(0) == 1:
                    sudoku[i][j] = 45 - sum(sudoku[i])
                else:
                    zero = 0
                    sumV = 0
                    for ii in range(9):
                        if sudoku[ii][j] == 0:
                            zero += 1
                        sumV += sudoku[ii][j]
                    if zero == 1:
                        sudoku[i][j] = 45 - sumV
                    else:
                        row, col = i//3*3, j//3*3
                        zero = 0
                        sumV = 0
                        for x in range(row, row+3):
                            for y in range(col, col+3):
                                if sudoku[x][y] == 0:
                                    zero += 1
                                sumV += sudoku[x][y]
                        if zero == 1:
                            sudoku[i][j] = 45 - sumV
for _ in range(9):
    print(*sudoku[_])