# 숫자판 점프
from itertools import product

area = [list(map(int, input().split())) for _ in '_'*5]

cnt = 0
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
num_list = []
for i in range(5):
    for j in range(5):
        for p in list(product([0, 1, 2, 3], repeat=5)):
            num = [area[i][j]]
            ni, nj = i, j
            for k in p:
                ni += delta[k][0]
                nj += delta[k][1]
                if 0 <= ni < 5 and 0 <= nj < 5:
                    num += [area[ni][nj]]
                else:
                    break
            else:
                if num in num_list:
                    continue
                else:
                    num_list += [num]
                    cnt += 1
print(cnt)
