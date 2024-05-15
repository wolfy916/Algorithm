eq_n = list(input())

stack_num = []
for x in eq_n:
    if x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        stack_num += [int(x)]
    else:
        if x == '+':
            stackV = stack_num[-2] + stack_num[-1]
        elif x == '-':
            stackV = stack_num[-2] - stack_num[-1]
        elif x == '*':
            stackV = stack_num[-2] * stack_num[-1]
        elif x == '/':
            stackV = stack_num[-2] // stack_num[-1]
        stack_num.pop()
        stack_num.pop()
        stack_num += [stackV]

print(stack_num[-1])