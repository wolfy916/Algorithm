T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    stack = [nums[-1]]
    benefit = 0
    for num in nums[-2::-1]:
        if stack[0] > num:
            stack += [num]
        elif stack[0] <= num:
            benefit += stack[0] * (len(stack) - 1)
            if len(stack) > 1:
                for x in stack[1:]:
                    benefit -= x
            stack = [num]
    else:
        benefit += stack[0] * (len(stack) - 1)
        if len(stack) > 1:
            for x in stack[1:]:
                benefit -= x
        stack = []

    print(f'#{tc} {benefit}')