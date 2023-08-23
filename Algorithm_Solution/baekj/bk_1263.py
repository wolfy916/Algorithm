# 시간 관리
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 정렬 후, 누적합
def solution(N, schedule):
    schedule.sort(key=lambda x: x[1])
    answer = 1000001
    for i in range(N - 1):
        schedule[i+1][0] += schedule[i][0]
        answer = min(answer, schedule[i][1] - schedule[i][0])
    answer = min(answer, schedule[N-1][1] - schedule[N-1][0])
    return answer if answer > -1 else -1

# [main]
if __name__ == '__main__':
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, schedule))