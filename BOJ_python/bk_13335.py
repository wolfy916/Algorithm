# 트럭
import sys
input = sys.stdin.readline

# n : 트럭 수, w : 다리 길이, L : 다리 최대 하중
n, w, L = map(int, input().split())
line = list(map(int, input().split()))  # line : 트럭 리스트

time = 0
q = [0] * w  # 다리 위의 상태 0은 빈 공간
i = 0
while i != n:  # 마지막 트럭이 인큐되면 종료
    time += 1
    q.pop(0)  # 디큐
    if sum(q) + line[i] <= L:
        q += [line[i]]  # 조건에 맞으면 인큐
        i += 1
    else:
        q += [0]  # 조건에 안맞으면 빈 공간을 의미하는 0 인큐

print(time + w)  # 마지막 트럭을 보내기 위해 다리 길이를 더함
