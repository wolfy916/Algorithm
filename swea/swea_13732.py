# 정사각형 판정
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(input()) for _ in '_'*N]

    # 내가 풀었던 방법
    # num = 0
    # result = 'yes'
    # for i in range(N):
    #     for j in range(N):
    #         if area[i][j] == '#' and num == 0:
    #             delta = 1
    #             width = 1
    #             height = 1
    #             while True:
    #                 if 0 <= j + delta < N and 0 <= i + delta < N:
    #                     if area[i][j+delta] == '#':
    #                         width += 1
    #                     if area[i+delta][j] == '#':
    #                         height += 1
    #                     if area[i][j+delta] == '.' or j+delta == N-1:
    #                         break
    #                     if area[i+delta][j] == '.' or i+delta == N-1:
    #                         break
    #                 else:
    #                     break
    #                 delta += 1
    #             if width == height:
    #                 for k in range(i, i+height):
    #                     for l in range(j, j+width):
    #                         if area[k][l] == '#':
    #                             area[k][l] = '.'
    #                             num += 1
    #                 if width**2 != num:
    #                     result = 'no'
    #             elif width != height:
    #                 result = 'no'
    #         elif area[i][j] == '#' and num != 0:
    #             result = 'no'
    #             break

    a = b = 21
    c = d = -1
    result = 'yes'
    for i in range(N):
        for j in range(N):
            if area[i][j] == '#':
                a, b, c, d = min(a, i), min(b, j), max(c, i), max(d, j)

    if c-a != d-b:
        result = 'no'

    for k in range(a, c+1):
        for l in range(b, d+1):
            if area[k][l] != '#':
                result = 'no'

    print(f'#{tc} {result}')