# 숫자판 점프
from itertools import product  # product : 숫자 중복 허용 순열

area = [list(map(int, input().split())) for _ in '_'*5]

cnt = 0
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 5번을 이동하기 위한 delta
num_list = []  # 완성된 숫자들을 할당할 리스트
for i in range(5):
    for j in range(5):
        for p in list(product([0, 1, 2, 3], repeat=5)):  # p : 많은 순열 중 하나
            num = [area[i][j]]  # 숫자를 완성하기 위한
            ni, nj = i, j
            for k in p:  # p : delta를 사용하기 위한 인덱스 순열
                ni += delta[k][0]
                nj += delta[k][1]
                if 0 <= ni < 5 and 0 <= nj < 5:  # 유효 인덱스 검사
                    num += [area[ni][nj]]        # 숫자 추가
                else:      # 유효한 인덱스가 아니라면
                    break  # 6개의 숫자를 완성하는 도중에 break
            else:  # break 없이 정상적으로 for문을 종료하여 숫자 완성했을 경우
                if num in num_list:  # 완성한 숫자가 이미 있다면 continue
                    continue
                else:
                    num_list += [num]  # 추가
                    cnt += 1  # 완성된 숫자 갯수 + 1
print(cnt)