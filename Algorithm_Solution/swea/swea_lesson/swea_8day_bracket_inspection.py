# 괄호 검사

T = int(input())
for tc in range(1, T+1):
    line = list(input())  # input

    STACK = []  # 스택 빈리스트 생성
    for x in line:
        if x == '{' or x == '(':  # 열린 괄호 발견 시 push
            STACK += [x]
        elif x == '}':  # 닫힌 중괄호 발견 시 pop
            if len(STACK) != 0 and STACK[-1] == '{':
                STACK.pop()
            else:
                STACK += [x]
                break
        elif x == ')':  # 닫힌 소괄호 발견 시 pop
            if len(STACK) != 0 and STACK[-1] == '(':
                STACK.pop()
            else:
                STACK += [x]
                break

    if len(STACK) != 0:  # 스택의 길이 검사 및 출력
        result = 0
    elif len(STACK) == 0:
        result = 1

    print(f'#{tc} {result}')