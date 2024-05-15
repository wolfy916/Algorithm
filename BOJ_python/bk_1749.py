# 점수따먹기
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 로직함수
def solution(N, M, matrix):
    # [B-1] 2차원 누적합
    for i in range(N+1):
        for j in range(1, M+1):
            matrix[i][j] += matrix[i][j-1]
    for j in range(M+1):
        for i in range(1, N+1):
            matrix[i][j] += matrix[i-1][j]
    # [B-3] 모든 부분 행렬 합 계산
    answer = matrix[1][1]
    for i in range(N+1):
        for j in range(M+1):
            for x in range(i+1, N+1):
                for y in range(j+1, M+1):
                    v1 = matrix[x][y]
                    v2 = matrix[i][y]
                    v3 = matrix[x][j]
                    v4 = matrix[i][j]
                    sumV = v1 - v2 - v3 + v4
                    answer = max(answer, sumV)
    return answer

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, matrix))