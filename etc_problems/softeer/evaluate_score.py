# 소프티어 성적 평가
import sys

# [A] 메인 함수
def solution():
    # [B] 입력 초기화 함수
    def input():
        return sys.stdin.readline().rstrip('\n')

    # [1] 데이터 입력 및 초기화
    n = int(input())
    contest = [[] for _ in range(4)]
    for i in range(3):
        contest[i] = list(map(int, input().split()))
    contest[3] = [contest[0][i] + contest[1][i] + contest[2][i] for i in range(n)]

    # [2] 각 대회의 순위 산출
    ranking = [[0] * n for _ in range(4)]
    for i in range(4):
        scores = [0] * 4001
        # [2-1] 점수를 인덱스로 사람수를 기록
        for score in contest[i]:
            scores[score] += 1

        # [2-2] 역방향 누적합
        for j in range(3999, -1, -1):
            scores[j] += scores[j + 1]

        # [2-3] rank 설명
        #  1. 나보다 높은 점수가 존재하지 않는 최고 점수(4번째 대회의 최고점 4000점)라면 1등
        #  2. 바로 앞점수(내 점수 + 1)까지의 누적 인원수 + 1 = 나의 순위
        for j in range(n):
            rank = 1 if contest[i][j] == 4000 else scores[contest[i][j] + 1] + 1
            ranking[i][j] = rank

    # [3] 출력 포멧
    for i in range(4):
        ranking[i] = " ".join(map(str, ranking[i]))

    return "\n".join(ranking)


# 메인 함수 실행
print(solution())