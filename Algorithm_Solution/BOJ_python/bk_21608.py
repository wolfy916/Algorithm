# 상어 초등학교
import sys

def input():
    return sys.stdin.readline().rstrip()

def sit_down(n, i, j):
    seats[i][j] = n
    sitting[n] = [i, j]
    empty[i][j] = -1
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
        if seats[ni][nj]: continue
        empty[ni][nj] -= 1

def solution():
    for n, *nums in table:
        like = dict()
        for m in nums:
            if sitting[m][0] < 0: continue
            mi, mj = sitting[m]
            for di, dj in delta:
                ni, nj = mi + di, mj + dj
                if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
                if seats[ni][nj]: continue
                if like.get((ni, nj)):
                    like[(ni, nj)] += 1
                else:
                    like[(ni, nj)] = 1

        vi, vj = -1, -1

        if len(like.keys()) > 0:
            maxV = -1
            coords = []
            for key in like.keys():
                if maxV < like[key]:
                    maxV = like[key]
                    coords = [key]
                elif maxV == like[key]:
                    coords.append(key)
            coords.sort(key=lambda x: [x[0], x[1]])
            maxV = -1
            for i, j in coords:
                if maxV < empty[i][j]:
                    maxV = empty[i][j]
                    vi, vj = i, j
        else:
            maxV = -1
            for i in range(N):
                for j in range(N):
                    if seats[i][j]: continue
                    if maxV < empty[i][j]:
                        maxV = empty[i][j]
                        vi, vj = i, j

        sit_down(n, vi, vj)

    answer = 0
    for i in range(N):
        for j in range(N):
            n = seats[i][j]
            like = None
            for m, *like in table:
                if n != m: continue
                like = like
                break
            tmp = 0
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
                if seats[ni][nj] in like:
                    tmp += 1
            if tmp:
                answer += 10 ** (tmp - 1)

    return answer

if __name__ == '__main__':
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N ** 2)]

    empty = [[4] * N for _ in range(N)]
    empty[0][0] = 2
    empty[N - 1][0] = 2
    empty[0][N - 1] = 2
    empty[N - 1][N - 1] = 2
    for i in range(1, N - 1):
        empty[0][i] = 3
        empty[N - 1][i] = 3
        empty[i][0] = 3
        empty[i][N - 1] = 3

    seats = [[0] * N for _ in range(N)]
    sitting = {i: [-1, -1] for i in range(1, N ** 2 + 1)}
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

    print(solution())