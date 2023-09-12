# 흩날리는 시험지 속에서 내 평점이 느껴진거야
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B-1] mid값의 유효성 검사 함수
def check1(mid, N, K):
    minV = float('inf')
    sumV = cnt = 0
    for i in range(N):
        if sumV < mid and N - i >= K - cnt:
            sumV += scores[i]
        else:
            minV = min(minV, sumV)
            sumV = scores[i]
            cnt += 1
        if cnt == K - 1: break
    minV = min(minV, sum(scores[i:]) if cnt else sumV)
    return True if minV >= mid else False

# [B-2] 다른 방식의 검사방법
def check2(mid, N, K):
    cnt = sumV = 0
    for i in range(N):
        sumV += scores[i]
        if sumV >= mid:
            sumV = 0
            cnt += 1
    return cnt > K - 1

# [C] 이분 탐색 함수
def solution(N, K):
    if K == 1: return sum(scores)
    answer = 0
    left, right = 0, sum(scores)
    while left <= right:
        mid = (left + right) // 2
        if check2(mid, N, K):
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    return answer

# [main]
if __name__ == '__main__':
    N, K = map(int, input().split())
    scores = tuple(map(int, input().split()))
    print(solution(N, K))