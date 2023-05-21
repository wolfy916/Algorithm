# 파리퇴치 3

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]  # 파리 구역 2차원 리스트로 할당

    plus_direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # + 합산을 위한 델타값들
    multiple_direction = [[-1, -1], [-1, 1], [1, 1], [1, -1]]  # X 합산을 위한 델타값들

    maxV = 0
    for i in range(N):
        for j in range(N):
            plus_sumV = area[i][j]  # 기준값을 미리 넣어놓기
            multiple_sumV = area[i][j]  # 기준값을 미리 넣어놓기
            k = 1  # 델타값을 몇번 적용시킬지 k로 제어
            while k != M:  # 스프레이 세기와 k를 비교하여 탈출문 제어
                for a, b in plus_direction:
                    if 0 <= i+a*k < N and 0 <= j+b*k < N:  # 델타값을 적용한 값이 인덱스내에 존재하는지 검사
                        plus_sumV += area[i+a*k][j+b*k]
                for c, d in multiple_direction:
                    if 0 <= i+c*k < N and 0 <= j+d*k < N:  # 델타값을 적용한 값이 인덱스내에 존재하는지 검사
                        multiple_sumV += area[i+c*k][j+d*k]
                k += 1

            if plus_sumV <= multiple_sumV:  # maxV 계산
                if maxV < multiple_sumV:
                    maxV = multiple_sumV
            else:
                if maxV < plus_sumV:
                    maxV = plus_sumV

    print(f'#{tc} {maxV}')