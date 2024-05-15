# 용액
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 이분 탐색
def bin_search(data, N):
    answer = [0, 0]
    value = float('inf')
    for p1 in range(N - 1):
        left, right = p1 + 1, N - 1
        while left <= right:
            p2 = (left + right) // 2
            tmp = data[p1] + data[p2]

            # 더 작은 절댓값으로 갱신
            if abs(tmp) < value:
                answer[0], answer[1] = data[p1], data[p2]
                value = abs(tmp)

            # 합이 음수이면 left 이동
            if tmp < 0:
                left = p2 + 1
            # 합이 양수이면 right 이동
            else:
                right = p2 - 1

    return answer

# [main]
if __name__ == '__main__':
    N = int(input())
    data = list(map(int, input().split()))
    print(*bin_search(data, N))