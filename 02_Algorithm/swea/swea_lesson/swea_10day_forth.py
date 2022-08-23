T = int(input())
for tc in range(1, T+1):
    line = list(input().split())

    if line[0] in ['*', '+', '-', '/']:
        result = 'error'
        print(f'#{tc} {result}')
        continue
    else:
        stack = [int(line[0])]

    i = 1
    while line[i] != '.':  # 입력받은 line의 마지막 원소인 '.'가 나오면 종료

        if line[i] in ['*', '+', '-', '/']:  # 연산 기호일 경우
            if len(stack) == 1:  # 연산기호를 탐색하였는데 stack에 숫자가 1개 밖에 없을 경우 error
                result = 'error'
                break
            a = stack.pop()
            b = stack.pop()
            if line[i] == '+':
                stack += [b + a]
            elif line[i] == '-':
                stack += [b - a]
            elif line[i] == '/':
                stack += [b // a]
            elif line[i] == '*':
                stack += [b * a]

        else:  # 숫자일 경우
            stack += [int(line[i])]
        i += 1

    else:  # while문 정상적 종료 시 실행
        if len(stack) == 1:
            result = stack.pop()
        else:
            result = 'error'

    print(f'#{tc} {result}')