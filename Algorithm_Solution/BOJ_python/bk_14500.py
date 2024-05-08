# 테트로미노
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in '_'*N]

type1 = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)]]
type2 = [[(0, 0), (1, 0), (0, 1), (1, 1)]]
type3 = [[(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (1, 0), (0, 1), (0, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (1, -1), (1, -2)]]
type3_sym = [[(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (1, 0), (2, 0)],[(0, 0), (0, 1), (0, 2), (1, 2)]]
type4 = [[(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (-1, 1), (-1, 2)]]
type4_sym = [[(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)]]
type5 = [[(0, 0), (1, 0), (0, -1), (-1, 0)], [(0, 0), (1, 0), (0, -1), (0, 1)], [(0, 0), (1, 0), (-1, 0), (0, 1)], [(0, 0), (0, -1), (-1, 0), (0, 1)]]

all_type = type1 + type2 + type3 + type3_sym + type4 + type4_sym + type5
maxV = 0
for i in range(N):
    for j in range(M):
        for shape in all_type:
            sumV = 0
            for di, dj in shape:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += area[ni][nj]
                else:
                    break
            else:
                if maxV < sumV:
                    maxV = sumV
print(maxV)