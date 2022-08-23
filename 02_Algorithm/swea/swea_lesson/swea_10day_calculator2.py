for tc in range(1, 11):
    N = int(input())
    line = list(input())

    # 곱하기가 필요한 숫자들을 모두 곱셈을 해놓고, 마지막에 싹 다 더하기
    plus_num_stack = []
    plus_sign_cnt = 0

    multiple_num_stack = []
    multiple_sign_cnt = 0

    for char in line:
        if char == '+':  # 덧셈이라면?
            plus_sign_cnt += 1  # 덧셈 연산자 개수 추가
            if multiple_sign_cnt != 0:  # 곱하기 개수가 0이 아니라면 !
                while multiple_sign_cnt:  # 곱하기 개수를 모두 소모하여 곱셈 !
                    multiple_num_stack += [multiple_num_stack.pop() * multiple_num_stack.pop()]
                    multiple_sign_cnt -= 1
                plus_num_stack += [multiple_num_stack.pop()]  # 곱셈이 끝난 숫자를 덧셈 숫자 스택에 push

        elif char == '*':  # 곱셈이라면?
            if not multiple_num_stack:  # 곱셈을 해야할 숫자들의 스택이 비어있다면 덧셈 숫자 스택에서 하나를 가져옴
                multiple_num_stack += [plus_num_stack.pop()]
            multiple_sign_cnt += 1  # 곱하기 연산자 개수 추가

        else:  # 숫자라면?
            if multiple_sign_cnt == 0:  # 곱하기 개수가 0이라면 덧셈 숫자 스택에 push
                plus_num_stack += [int(char)]
            else:  # 곱하기 개수가 0이 아니라면 곱셈 숫자 스택에 push
                multiple_num_stack += [int(char)]

    if multiple_sign_cnt != 0:  # 마지막에 곱하기만 push 하다가 연산안하고 끝나는것을 방지
        while multiple_sign_cnt:
            multiple_num_stack += [multiple_num_stack.pop() * multiple_num_stack.pop()]
            multiple_sign_cnt -= 1
        plus_num_stack += [multiple_num_stack.pop()]

    sumV = 0
    for x in plus_num_stack:  # 남은 숫자 모두 더하기~
        sumV += x

    print(f'#{tc} {sumV}')