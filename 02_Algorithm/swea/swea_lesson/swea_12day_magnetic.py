T = 10
for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in '_'*100]

    cnt = 0
    for j in range(100):
        stack_i = []
        for i in range(100):
            if table[i][j] == 1:
                stack_i += [i]
            elif table[i][j] == 2 and stack_i:
                if i > stack_i.pop():
                    stack_i.clear()
                    cnt += 1
        else:
            stack_i.clear()

    print(f'#{tc} {cnt}')


