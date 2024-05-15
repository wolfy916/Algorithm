T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]  # N by N 2차원 리스트 할당

    maxV = 0
    for i in range(N):
        for j in range(N):
            sumV = 0  # 합을 할당할 변수 초기화
            for k in range(N):
                sumV += area[i][k]  # 가로 원소들 합산
                sumV += area[k][j]  # 세로 원소들 합산
            if maxV < sumV - area[i][j]:  # 합산한 값에서 중복 원소 값 제거하여 maxV에 비교 및 할당
                maxV = sumV - area[i][j]

    print(f'#{tc} {maxV}')
