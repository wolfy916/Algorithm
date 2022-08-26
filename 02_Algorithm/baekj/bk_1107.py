# 리모컨
def big_goal(l, z):  # l : len_target, z : zero

    if z == 0:
        goal = [min(passes)] * (l + 1)
    else:
        goal = [min(passes[1:])] + [0] * l

    return int(''.join(list(map(str, goal))))


def normal_goal1(t, l):  # t : target_list , l : len_target

    goal = []
    goal_ = []
    for j in range(l):
        absv_list = []
        use_num = []
        for pass_num in passes:
            absv_list += [abs(target_list[j] - pass_num)]
            use_num += [pass_num]
        min_absv = min(absv_list)
        for i in range(len(absv_list)):
            if absv_list[i] == min_absv:
                select_num = use_num[i]
                if j+1 == len(goal_):
                    goal_.pop()
                goal_ += [select_num]
                if goal_[-1] > target_list[j]:
                    goal1 = goal_[:len(goal_)]
                    goal1 += [min(passes)] * (l-len(goal_))
                    goal += [int(''.join(list(map(str, goal1))))]
                elif goal_[-1] < target_list[j]:
                    goal2 = goal_[:len(goal_)]
                    goal2 += [max(passes)] * (l-len(goal_))
                    goal += [int(''.join(list(map(str, goal2))))]
                else:
                    pass
    if not goal:
        return [int(''.join(list(map(str, goal_))))]
    return goal

def normal_goal2(l):  # l : len_target

    goal = []
    for pass_num in passes:
        if pass_num > target_list[0]:
            goal += [pass_num]
            break
    goal += [min(passes)] * (l-1)

    return int(''.join(list(map(str, goal))))

def normal_goal3(l):  # l : len_target

    goal = []
    for pass_num in passes[::-1]:
        if pass_num < target_list[0]:
            goal += [pass_num]
            break
    goal += [max(passes)] * (l-1)

    return int(''.join(list(map(str, goal))))


def small_goal(l):  # l : len_target

    goal = [max(passes)] * (l - 1)

    return int(''.join(list(map(str, goal))))

target = int(input())
error_num = int(input())
if error_num == 0:
    pass
else:
    errors = list(map(int, input().split()))

current = 100
target_str = str(target)                  # 목표 채널 -> string
target_list = list(map(int, target_str))  # 목표 채널 -> int형 원소들의 list
len_target = len(target_str)              # 목표 채널값의 자릿수
target_absV = abs(target-current)         # 목표 채널과 현재 채널과의 차이

passes = []  # 정상 작동하는 버튼
if error_num == 0:
    passes = list(map(int, range(0, 10)))
else:
    for num in range(10):
        if num not in errors:
            passes += [num]

if 0 in passes:  # 숫자 0 버튼의 정상작동 유무
    zero = 1  # 정상 작동
else:
    zero = 0  # 고장

goal_list = []  # 정답 후보들을 담을 리스트

#1 고장난 버튼 수 = 0
if error_num == 0:
    if target_absV >= len_target:
        result = len_target
    elif target_absV < len_target:
        result = target_absV

#1 고장난 버튼 수 != 0
elif error_num != 10 and not(error_num == 9 and zero == 1):
    #2 목표채널의 자릿수
    if len_target == 1:
        goal_list += normal_goal1(target_list, len_target)
        goal_list += [big_goal(len_target, zero)]
    elif 1 < len_target < 4:
        goal_list += [big_goal(len_target, zero)]
        goal_list += normal_goal1(target_list, len_target)
        goal_list += [normal_goal2(len_target)]
        goal_list += [normal_goal3(len_target)]
        goal_list += [small_goal(len_target)]
        goal_list += [current]
    else:
        goal_list += [big_goal(len_target, zero)]
        goal_list += normal_goal1(target_list, len_target)
        goal_list += [normal_goal2(len_target)]
        goal_list += [normal_goal3(len_target)]
        goal_list += [small_goal(len_target)]

else:
    pass

if target == current:
    result = 0

elif error_num == 0:
    pass

elif error_num == 10:
    result = abs(target - current)

elif error_num == 9 and zero == 1:
    if target == 0:
        result = 1
    elif 0 < target < 50:
        result = target + 1
    else:
        result = abs(target - current)

else:
    goal_absV = []
    for x in goal_list:
        lenx = len(str(x))
        if x != 100:
            goal_absV += [abs(target-x) + lenx]
        else:
            goal_absV += [abs(target-x)]
    result = min(goal_absV)

print(result)