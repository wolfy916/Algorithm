# 달력
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    # 데이터 입력 및 초기화
    N = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(N)]
    schedule.sort(key=lambda x: [x[0], x[0] - x[1]])

    # 달력 생성 및 일정 표기
    calendar = [0] * 366
    for s, e in schedule:
        for i in range(s, e + 1):
            calendar[i] += 1

    # 코팅지 넓이 합산
    answer = 0
    w, h = 0, 1
    for i in range(1, 366):
        if calendar[i] == 0:
            answer += w * h
            w, h = 0, 1
        else:
            w += 1
            h = max(h, calendar[i])
    if w > 0:
        answer += w * h

    print(answer)