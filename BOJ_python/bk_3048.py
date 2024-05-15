# 개미

N1, N2 = map(int, input().split())  # 각 개미수
N1_line = list(input())[::-1]       # N1 개미들 reverse 리스트 할당
N2_line = list(input())             # N2 개미들 리스트 할당
T = int(input())                    # T는 시간, 0 ≤ T ≤ 50

line = N1_line + N2_line  # T = 0초 일때의 배열

while T:  # 시간 모두 소진시키면 종료
    change = 0
    for i in range(0, N1+N2-1):  # line의 모든 원소를 탐색
        if change == 1:          # 개미 한마리가 단위시간내에서 여러번 이동 하는 것을 방지
            change = 0           #
            continue             #
        if line[i] in N1_line and line[i+1] in N2_line:  # 서로 다른 그룹일 경우
            line[i], line[i+1] = line[i+1], line[i]      # 자리 이동
            change = 1                                   # 자리를 이동한 개미임을 표시
    T -= 1  # 시간 1초씩 소진

print(''.join(line))  # 문자열로 출력