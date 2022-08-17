# 파스칼의 삼각형

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    area = [[] for _ in range(N)]  # 2차원 빈 리스트 생성
    for i in range(N):  # N행 반복
        if i == 0:
            area[i] += [1]  # 첫번째 행일 때 원소 1 할당
        else:
            for j in range(i+1):  # 예 ) i = 1 (두번째 행)일때, j = i+1 (원소 2개)
                if j == 0:  # 첫번째 열과 마지막 열의 원소는 1
                    area[i] += [area[i-1][j]]
                elif j == i:
                    area[i] += [area[i-1][j-1]]
                else:  # 규칙에 따라 위의 행의 두개의 원소를 더함.
                    area[i] += [area[i-1][j-1]+area[i-1][j]]
        print(' '.join(list(map(str, area[i]))))  # 행이 완성될때마다 출력