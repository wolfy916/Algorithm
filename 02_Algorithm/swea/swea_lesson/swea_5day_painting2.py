# 스도쿠 검증
T = int(input())
for tc in range(1, T+1):
    area = [list(map(int, input().split())) for _ in range(9)] # 2차원 배열 생성

    for i in range(9): # 행 인덱스 탐색

        if len(set(area[i])) != 9: # 가로 줄을 set()로 바꾸어 중복 검사
            result = 0 # 길이가 9에서 줄었을 경우 result = 0
            break

        test_column = [] # 세로 줄을 검사하기 위한 리스트 초기화
        for j in range(9): # 열 인덱스 탐색
            test_column += [area[j][i]]  # 세로 줄에 해당하는 원소 추가
            test_area = [] # 3 X 3 을 검사하기 위한 리스트 초기화
            if i % 3 == 0 and j % 3 == 0: # 3 X 3 에서의 첫번째 인덱스 검사 ex) [0,0], [3,6], [6,0] 등등
                for k in range(i, i+3): # 3 X 3의 모든 원소를 test-area 에 추가
                    test_area += area[k][j:j+3]
                if i % 3 == 0 and len(set(test_area)) != 9: # 3 X 3의 원소들을 받은 리스트를 set() 중복 검사
                    result = 0
                    break

        if len(set(test_column)) != 9: # 세로 줄을 set() 중복 검사
            result = 0
            break
    else:
        result = 1 # 위의 모든 조건에 해당되지 않는다면 중복이 없으므로 result = 1

    print(f'#{tc} {result}')