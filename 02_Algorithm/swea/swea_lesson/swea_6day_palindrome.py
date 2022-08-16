# string 실습 회문

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(input()) for _ in range(N)]  # 각 알파벳을 원소로 받은 N by N 2차원 리스트 생성

    for i in range(N):
        for j in range(N-M+1):  # j : 단어 M의 길이로 N을 (N-M+1)번 탐색할 수 있다.

            # 가로 탐색
            if area[i][j:j+M] == area[i][j:j+M][::-1]:  # 슬라이싱으로 탐색
                result = area[i][j:j + M + 1]
                break

            # 세로 탐색
            test_line = []  # 세로 탐색을 위한 빈 리스트 초기화
            for k in range(M):
                test_line += [area[k+j][i]]  # 해당하는 원소를 모두 넣어서 검사
            if test_line == test_line[::-1]:
                result = test_line
                break
    result = ''.join(result)
    print(f'#{tc} {result}') # 리스트를 string으로 묶어서 출력
