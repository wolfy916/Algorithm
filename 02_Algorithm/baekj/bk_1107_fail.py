# 리모컨

target = int(input())
error_num = int(input())
errors = list(map(int, input().split()))

current = 100
target_str = str(target)  # 목표 채널 -> string
target_list = list(map(int, target_str))  # 목표 채널 -> 정수형 list
len_target = len(target_str)  # 목표 채널이 몇자리수?
target_absV = abs(target-current)  # 목표 채널과 현재 채널과의 차이

passes = []  # 정상 작동하는 버튼
for num in range(10):
    if num not in errors:
        passes += [num]

goal_list = []  # 정답 후보들을 담을 리스트








