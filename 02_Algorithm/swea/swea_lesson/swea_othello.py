# 오셀로 게임

def attack(i, j, c):

    board[i][j] = c
    k = 0
    while k != 8:
        row = i + delta[k][0]
        col = j + delta[k][1]
        test = []
        while 0 <= row < N and 0 <= col < N and board[row][col] != 0:
            if board[row][col] != c:
                test += [[row, col, 'N']]
            else:
                test += [[row, col, 'Y']]
                break
            row += delta[k][0]
            col += delta[k][1]

        if len(test) > 1:
            if test[0][2] == 'N' and test[-1][2] == 'Y':
                for x, y, match in test:
                    if match == 'N':
                        board[x][y] = c
        k += 1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    board = [[0]*N for _ in '_'*N]
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2] = 2
    board[N//2][N//2-1] = 1

    delta = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

    for _ in '_' * M:
        j, i, color = map(int, input().split())
        attack(i-1, j-1, color)

    B = W = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                B += 1
            elif board[i][j] == 2:
                W += 1

    print(f'#{tc} {B} {W}')