# 캐슬 디펜스
# 조합 귀찮아서 갓터툴...
from itertools import combinations
import copy
import sys

input = sys.stdin.readline


# 사격
# 동시 사격에 대해 생각해야함
def fire(vi, vj):
    global check

    if area[vi][vj]:
        if area[vi][vj] == 2:  # 동시사격이라면 return 0
            return 0
        area[vi][vj] = 2
        check.append([vi, vj])
        return 1

    d = 1
    while d < D:

        ni, nj = vi, vj - d  # 왼쪽부터 탐색
        if 0 <= ni < N and 0 <= nj < M and area[ni][nj]:
            if area[ni][nj] == 2:
                return 0
            area[ni][nj] = 2
            check.append([ni, nj])
            return 1

        # 마름모 탐색기법으로 북동, 남동방향으로 탐색
        for di, dj in delta:
            for _ in '_' * d:
                ni += di
                nj += dj
                if 0 <= ni < N and 0 <= nj < M and area[ni][nj]:
                    if area[ni][nj] == 2:
                        return 0
                    area[ni][nj] = 2
                    check.append([ni, nj])
                    return 1
        d += 1
    return 0


N, M, D = map(int, input().split())
battleground = [list(map(int, input().split())) for _ in '_' * N]

delta = [[-1, 1], [1, 1]]
maxV_result = 0
positions = list(combinations(list(range(M)), 3))
for position in positions:  # 궁수 배치의 모든 경우를 탐색
    area = copy.deepcopy(battleground)
    result = 0
    for i in range(N - 1, -1, -1):  # 마지막 행부터 사격하며 궁수가 올라옴
        check = []
        for j in range(M):
            if j in position:
                result += fire(i, j)
        for ci, cj in check:  # 하나의 행 사격 종료 후 사격이 이루어진 곳을 0으로 바꿈
            area[ci][cj] = 0

    if maxV_result < result:  # 최대값 연산
        maxV_result = result

print(maxV_result)