'''
편의점 2 - 백준 실버2
분류 : 정렬, 수학
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 중간값 좌표 계산
def cal_position():
    position.sort(key=lambda x: x[0])
    x = position[N // 2][0]
    position.sort(key=lambda x: x[1])
    y = position[N // 2][1]
    return x, y

# [main]
if __name__ == '__main__':
    # [1] 데이터 입력
    N = int(input())
    position = [tuple(map(int, input().split())) for _ in range(N)]

    # [2] 좌표 계산
    X, Y = cal_position()

    # [3] 거리합 계산
    sumX = sum(map(lambda x: abs(x[0] - X), position))
    sumY = sum(map(lambda x: abs(x[1] - Y), position))

    print(sumX + sumY)