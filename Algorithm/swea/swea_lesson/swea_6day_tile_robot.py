T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]  # 색칠해야할 타일의 좌표를 리스트로 입력

    area = [[0] * 10 for _ in range(10)]
    cnt = 0
    for k in range(N):
        for i in range(10):
            for j in range(10):
                if line[k][0] <= i <= line[k][2] and line[k][1] <= j <= line[k][3]:  # 인덱스가 색칠해야할 영역에 속하는지 검사
                    if area[i][j] == 0:  # 색칠하고 카운트
                        area[i][j] += 1
                        cnt += 1
                    else:
                        area[i][j] += 1  # 색칠되어있다면 (= 해당 값이 0이 아니라면)

    print(f'#{tc} {cnt}')