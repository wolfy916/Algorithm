# 텀 프로젝트
# 나의 풀이 -> 시간 초과
from sys import stdin
input = stdin.readline

for tc in range(1, int(input())+1):
    N = int(input())                             # 학생의 수(2 ≤ n ≤ 100,000)
    arr = [0] + list(map(int, input().split()))  # 각 학생이 선택한 학생 리스트

    cnt = 0
    for i in range(1, N+1):
        if arr[i]:
            test = [i]
            cnt += 1
            while test:
                m = test[-1]

                if arr[m] == test[-1] or arr[m] == 0:
                    cnt -= 1
                    for num in test:
                        arr[num] = 0
                    break

                elif arr[m] in test:
                    cnt -= len(test[test.index(arr[m]):])
                    for num in test:
                        arr[num] = 0
                    break

                else:
                    test.append(arr[m])
                    cnt += 1

    print(cnt)