# 반복문자 제거하기

T = int(input())
for tc in range(1, T+1):
    line = list(input())

    STACK = []
    for x in line:
        if len(STACK) == 0:  # 스택이 비어있으면 push
            STACK += [x]
        else:
            if STACK[-1] != x:  # 스택의 원소와 비교하여 다르면 push
                STACK += [x]
            elif STACK[-1] == x:  # 스택의 원소와 비교하여 같으면 pop
                STACK.pop()

    print(f'#{tc} {len(STACK)}')