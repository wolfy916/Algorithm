# string 실습 회문 2
for _ in range(10):
    tc = int(input())
    area = [list(input()) for __ in range(100)]  # 각 알파벳을 원소로 받은 100 by 100 2차원 리스트 생성

    result = 0
    for str_len in range(100, 0, -1):
        for i in range(100):
            for j in range(100-str_len+1):  # j : 단어 str_len의 길이로 N을 (100-str_len+1)번 탐색할 수 있다.

                # 가로 탐색
                if area[i][j:j+str_len] == area[i][j:j+str_len][::-1]:  # 슬라이싱으로 탐색
                    result = str_len
                    break

                # 세로 탐색
                test_line = []  # 세로 탐색을 위한 빈 리스트 초기화
                for k in range(str_len):
                    test_line += [area[k+j][i]]  # 해당하는 원소를 모두 넣어서 검사
                if test_line == test_line[::-1]:
                    result = str_len
                    break

            if result == str_len:
                break
        if result == str_len:
            break

    print(f'#{tc} {result}')