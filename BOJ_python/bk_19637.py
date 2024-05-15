# IF문 좀 대신 써줘
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] (key, value) = (전투력 상한값, 칭호)를 갖는 dictionary와
#     전투력 상한값을 원소로 갖는 배열 생성
def trans_data(titles):
    scores = []
    ref = dict()
    for title in titles:
        name, score = title.split()
        score = int(score)
        if ref.get(score):
            ref[score].append(name)
        else:
            ref[score] = [name]
        scores.append(score)
    return scores, ref

# [C] 알맞은 칭호를 찾는 이분 탐색 함수
def bin_search(power, scores):
    left, right = 0, len(scores) - 1
    while left <= right:
        mid = (left + right) // 2
        if power > scores[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return scores[left] if power > scores[mid] else scores[mid]

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    titles = [input() for _ in range(N)]
    powers = [int(input()) for _ in range(M)]
    scores, ref = trans_data(titles)
    for power in powers:
        print(ref[bin_search(power, scores)][0])