for tc in range(1, 11):
    N = int(input())
    line = list(input())

    sign = ['+', '-', '/', '*', '(', ')']
    priority = {'+': [1, 1], '-': [1, 1], '*': [2, 2], '/': [2, 2], '(': [0, 3]}

    stack = []
    new_eqn = []
    for x in line:
        if x not in sign:
            new_eqn += [x]
        elif x == ')':
            while stack[-1] != '(':
                new_eqn += [stack.pop()]
            stack.pop()

        else:
            if not stack:
                stack += [x]
                continue
            else:
                if priority[x][1] > priority[stack[-1]][0]:
                    stack += [x]
                else:
                    while priority[x][1] <= priority[stack[-1]][0]:
                        new_eqn += [stack.pop()]
                    stack += [x]

    num_stack = []
    for y in new_eqn:
        if y == '+':
            b = num_stack.pop()
            a = num_stack.pop()
            num_stack += [a + b]
        elif y == '*':
            b = num_stack.pop()
            a = num_stack.pop()
            num_stack += [a * b]
        else:
            num_stack += [int(y)]

    print(f'#{tc} {num_stack[0]}')