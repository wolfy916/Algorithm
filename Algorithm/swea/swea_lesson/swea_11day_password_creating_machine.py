for tc in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))

    cnt = 0
    while password[-1] > 0:
        for i in range(1,6):
            test = password[0] - i
            if test <= 0:
                test = 0
                password = password[1:] + [test]
                break
            password = password[1:] + [test]
        cnt += 1

    print(f'#{tc} {" ".join(list(map(str,password)))}')