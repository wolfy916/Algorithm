# 케이크 자르기
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 임의의 롤케이크 조각 길이에 대한 유효성 검사
def check(mid, prev, cnt):
    if cnt == q:
        return True if L - S[prev] >= mid else False
    prev_s = S[prev] if prev >= 0 else 0
    for i in range(prev + 1, M - q + cnt + 1):
        s = S[i]
        if s - prev_s < mid: continue
        if check(mid, i, cnt + 1):
            return True
    return False

# [C] 이분 탐색 함수
def bin_search(tmp):
    answer = 0
    left, right = 1, tmp
    while left <= right:
        mid = (left + right) // 2
        if check(mid, -1, 0):
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    return answer

# [main]
if __name__ == '__main__':
    N, M, L = map(int, input().split())
    S = [int(input()) for _ in range(M)]
    tmp = L
    for _ in range(N):
        q = int(input())
        tmp = bin_search(tmp)
        print(tmp)