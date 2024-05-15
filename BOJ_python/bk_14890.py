# 경사로
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

def check_col(idx, a, b):
    if a < 0 or b >= N: return False
    if visited[a][idx]: return False
    tmp = area[a][idx]
    for i in range(a + 1, b + 1):
        if visited[i][idx]: return False
        if tmp != area[i][idx]: return False
    return True

def check_row(idx, a, b):
    if a < 0 or b >= N: return False
    if visited[idx][a]: return False
    tmp = area[idx][a]
    for j in range(a + 1, b + 1):
        if visited[idx][j]: return False
        if tmp != area[idx][j]: return False
    return True

# [main]
if __name__ == '__main__':
    N, L = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        if i == 4:
            A = 1
        for j in range(N - 1):
            if area[i][j] - 1 == area[i][j+1]:
                if not check_row(i, j + 1, j + L):
                    break
                else:
                    for k in range(j + 1, j + L + 1):
                        visited[i][k] = True
            elif area[i][j] + 1 == area[i][j+1]:
                if not check_row(i, j - L + 1, j):
                    break
                else:
                    for k in range(j - L + 1, j + 1):
                        visited[i][k] = True
            elif abs(area[i][j] - area[i][j + 1]) > 1:
                break
        else:
            answer += 1

    visited = [[False] * N for _ in range(N)]
    for j in range(N):
        for i in range(N - 1):
            if area[i][j] - 1 == area[i + 1][j]:
                if not check_col(j, i + 1, i + L):
                    break
                else:
                    for k in range(i + 1, i + L + 1):
                        visited[k][j] = True
            elif area[i][j] + 1 == area[i + 1][j]:
                if not check_col(j, i - L + 1, i):
                    break
                else:
                    for k in range(i - L + 1, i + 1):
                        visited[k][j] = True
            elif abs(area[i][j] - area[i + 1][j]) > 1:
                break
        else:
            answer += 1

    print(answer)