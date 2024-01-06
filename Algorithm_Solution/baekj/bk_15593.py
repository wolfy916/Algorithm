'''
Lifeguards (Bronze) - 백준 브론즈2
분류 : 완전 탐색, 누적합
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 로직 함수
def solution(lifeguards):
    # [1] 누적합을 위한 포인트 표기
    table = [0] * 1002
    for s, e in lifeguards:
        table[s] += 1
        table[e] -= 1

    # [2] table을 복사하여 특정 포인트를 제거하고
    #     누적합을 진행하며 answer값 갱신
    answer = 0
    for s, e in lifeguards:
        tmp = table[:]
        tmp[s] -= 1
        tmp[e] += 1
        for i in range(1, 1002):
            tmp[i] += tmp[i - 1]
        cnt = tmp.count(0)
        answer = max(answer, 1002 - cnt)

    return answer

# [Main]
if __name__ == '__main__':
    N = int(input())
    lifeguards = [tuple(map(int, input().split())) for _ in range(N)]

    print(solution(lifeguards))
