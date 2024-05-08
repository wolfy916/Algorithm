# 케이크 자르기
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 임의의 롤케이크 조각 길이에 대한 유효성 검사
def check(mid):
    cnt = prev = 0
    for i in range(M):
        if S[i] - prev < mid: continue
        cnt += 1
        prev = S[i]
    if cnt > q: return True
    elif cnt == q and L - prev >= mid: return True
    return False

# [C] 이분 탐색 함수
def bin_search(tmp):
    answer = 0
    left, right = 1, tmp
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            answer = mid
            left = mid + 1
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