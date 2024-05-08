# 문자열 게임 2
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 메인 로직 함수
def solution(W, K):
    # ref['a'] = [a가 위치한 인덱스들]
    ref = {}
    for i in range(len(W)):
        ref.setdefault(W[i], []).append(i)

    answer = [10001, 0]
    for v in ref.values():
        # 같은 문자 K개를 만족못하면 continue
        if len(v) < K: continue
        # K가 1이면 탐색할 필요가 없음
        if K == 1:
            answer = [1, 1]
            break
        else:
            # 길이 갱신
            idx = 0
            while idx + K - 1 < len(v):
                lenV = v[idx + K - 1] - v[idx] + 1
                answer[0] = min(answer[0], lenV)
                answer[1] = max(answer[1], lenV)
                idx += 1
    return answer if answer[0] < 10001 else [-1]

# [main]
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        W = list(input())
        K = int(input())
        print(*solution(W, K))