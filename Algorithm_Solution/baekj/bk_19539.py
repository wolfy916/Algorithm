# 사과나무
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 조건 판별 함수
#     1. 나무 높이의 전체 합이 3의 배수임을 만족하는지
#       -> 물뿌리개를 1, 2로 사용하든 3으로 사용하든 전체 총량은 3씩 늘어나기 때문
#     2. 높이를 2만큼 성장시키는 물뿌리개 사용횟수가 나무 높이를 3으로 나누었을때의 몫이상임을 만족하는지
#       -> 물뿌리개 1과 물뿌리개 2의 사용횟수는 같음
#       -> 위치에 관계없이 물을 주는 행위가 2번 행해진다면 높이의 전체 합이 1 x 2 + 2 x 2 = 6 만큼 자라는 것
#       -> 나무 높이의 전체 합은 조건 1을 만족하여 3의 배수이므로 3n
#       -> 3n = 1 x n + 2 x n 물을 주는 행위가 n번 행해져야함
#       -> 물뿌리개 2를 n번 이상만큼 사용할 수 있는지 카운트
#       (물뿌리개 2를 1회 사용하는 것은 물뿌리개 1을 2회 사용하는 것으로 대체 할 수 있다)
#       (따라서, 물뿌리개 2의 사용횟수를 카운트 했을때, n을 초과하는 횟수가 나와도 문제 없다)
def solution(N, heights):
    # [B-1] 조건 1 판별
    tot_sum = sum(heights)
    if tot_sum % 3: return 'NO'
    # [B-2] 조건 2 판별
    cnt = 0
    for i in range(N):
        cnt += heights[i] // 2
    return 'YES' if cnt >= tot_sum // 3 else 'NO'

# [main]
if __name__ == '__main__':
    N = int(input())
    heights = list(map(int, input().split()))
    print(solution(N, heights))