# 줄어드는 수
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 순서를 줄이며 탐색하는 함수
def search(p, num, order, N):
    # 순서가 일치할때까지
    while order != N:
        if num[p] > 0:
            num[p] -= 1
        else:
            tmp = 1
            # 다음 자릿수의 숫자가 줄어드는 조건을 충족하지 못하면
            # 그 다음 자릿수로 탐색
            while num[p - tmp] <= tmp:
                tmp += 1
            num[p - tmp] -= 1
            # 이전 자릿수들을 최대값으로 갱신
            for k in range(p - tmp + 1, p + 1):
                num[k] = num[k - 1] - 1
        order -= 1
    return ''.join(map(str, num))

# [C] 메인 로직 함수
def solution(N):
    # 1023개를 넘을 수 없음
    # dp로 미리 뽑은 숫자
    if N > 1023: return -1

    # dp[i][j] = j가 맨 앞자리로 오는 (i+1)자리 숫자의 경우의 수
    dp = [[0] * 10 for _ in range(10)]
    for j in range(10):
        dp[0][j] = 1  # j가 맨 앞자리로 오는 일의 자리 숫자는 1개씩 뿐임

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(j):
                dp[i][j] += dp[i - 1][k]

    order = 0
    for i in range(10):
        for j in range(10):
            order += dp[i][j]
            if order >= N:
                num = list(range(j, j - i - 1, -1))
                p = len(num) - 1
                return search(p, num, order, N)

# [main]
if __name__ == '__main__':
    N = int(input())
    print(solution(N))
