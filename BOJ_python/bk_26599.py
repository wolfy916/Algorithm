# 용 조련사 룰루
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [1] 데이터 입력 및 초기화
N, M = map(int, input().split())
P = list(map(int, input().split()))
# [1-1] 용이 한마리면 출력 & 종료
if N == 1:
    print("YES")
    print(P[0])
    exit()

# [2] 각 용의 힘을 기존 인덱스와 함께 파싱
#     용의 힘 기준, 오름차순 정렬
power = []
for i in range(1, N + 1):
    power.append((P[i - 1], i))
power.sort()

# [3] 나보다 약한 용 중에서 가장 강한 용의 힘과의 차이가 M 보다 큰 경우가 있다면
#     현재 나 자신보다 강한 용이 3마리 이상 있는지 확인 -> 없다면 NO 출력
#
#  ex) 6 10
#      10 20 50 60 70 80
#  (1) 50 - 20 > M = 10 을 확인
#  (2) 50 보다 강한 용이 3마리 있는지 인덱스로 확인(60, 70, 80이 있음)
#  (3) 옮길 수 있는 케이스로 판정
idx = 0
for i in range(N - 1, 0, -1):
    if power[i][0] - power[i - 1][0] > M:
        if N - i < 4 or N < 5:
            print('NO')
            exit()
        idx = i
        break

# [4] 3번의 조건에서 종료되지 않았다면 옮길 수 있다고 판단
#  ex) 6 10
#      10 20 50 60 70 80
print("YES")
# [4-1] 분기점(20과 50 사이)에 가장 가까운 우측 용 2마리만 남기고 강한 용은 모두 옮김(80, 70 이동)
for i in range(N - 1, idx + 1, -1):
    print(power[i][1], end=" ")
# [4-2] 분기점 기준 좌측 용들은 모두 옮김(20, 10 이동)
for i in range(idx - 1, -1, -1):
    print(power[i][1], end=" ")
# [4-3] 남아있던 두 마리 용을 옮김(50, 60 이동)
for i in range(idx + 1, idx - 1, -1):
    print(power[i][1], end=" ")