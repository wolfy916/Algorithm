# 괄호 짝맞추기 검사 !

T = int(input())
for tc in range(1, T+1):
    line = list(input())
    stack_list = []
    for i in line:
        if i == '(':
            stack_list += [i]
        elif i == ')':
            if len(stack_list) == 0:
                print(f'#{tc} 0')
                break
            else:
                stack_list.pop()
    else:
        if len(stack_list) == 0:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')