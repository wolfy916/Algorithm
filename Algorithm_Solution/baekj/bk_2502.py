# 떡 먹는 호랑이
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution(D, K):
    # [B-1] D번째 날에 A와 B가 각각 몇번씩 사용되는지 확인
    check = [[0, 0] for _ in range(D+1)]
    check[1][0] = 1  # 첫째날에는 A만 1개 사용됨
    check[2][1] = 1  # 둘째날에는 B만 1개 사용됨
    for i in range(3, D+1):
        check[i][0] = check[i-1][0] + check[i-2][0]
        check[i][1] = check[i-1][1] + check[i-2][1]

    # [B-2] K값을 만족하는 A, B 찾기
    for A in range(1, K):
        for B in range(A+1, K+1):
            v = A * check[D][0] + B * check[D][1]
            if v == K:
                return f"{A}\n{B}"
            elif v > K:
                break

# [main]
if __name__ == '__main__':
    D, K = map(int, input().split())
    print(solution(D, K))