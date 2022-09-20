# 입력값 설정
from sys import stdin
N = int(stdin.readline())
arr = [[] for _ in '_'*N]
for i in range(N):
    arr[i] = list(map(int, stdin.readline().split()))

cnt = 0 # 설치하지 못한 전기줄의 수 == 없애는 전깃줄의 수
cnt_list = [0]*N
# 밑을 N번 반복한다.
# arr.pop(0)해서 전기줄을 설치한다 (= lines.append)
# arr의 원소(A, B)에 대해서 lines의 원소(a, b)와 비교한다
# (A, B)가 (a, b)와 겹치는 지점이 없다면 전기줄을 설치한다 (= lines.append)
# 겹치는 지점이 있다면 설치하지 않는다 (cnt + 1)
# 비교가 끝나면 cnt값을 cnt_list에 저장하고 다시 arr에 append처리를 해준다.
for i in range(N):
    lines = []
    lines.append(arr.pop(0))

    for A, B in arr:
        flag = 0
        for a, b in lines:
            if A == a and B == b:
                break
            if A < a and B > b:
                cnt += 1
                break
            elif A > a and B < b:
                cnt += 1
                break
            else:
                flag += 1
                if flag == len(lines):
                    lines.append([A, B])
    cnt_list[i] = cnt
    cnt = 0
    arr.append(lines[0])
print(cnt_list)
print(min(cnt_list))