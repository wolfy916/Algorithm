import sys

# 오큰수

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

STACK = [nums[-1]]
result = [-1]

for num in nums[-2::-1]:

    STACK += [num]
    if STACK[0] > num:
        if len(STACK) > 2 and STACK[-2] > num:
            result += [STACK[-2]]
            STACK = STACK[1:]
        else:
            result += [STACK[0]]
    elif STACK[0] < num:
        result += [-1]
        STACK = [num]
    else:
        result += [-1]
        STACK = [num]


print(' '.join(list(map(str, result[::-1]))))