T = int(input())
for tc in range(1, T+1):
    num = int(input())
    nums = [2, 3, 5, 7, 11]
    line = [0]*5
    for i in range(5):
        while True:
            if not num % nums[i]:
                num = num // nums[i]
                line[i] += 1
            else:
                break

    print(f'#{tc} {" ".join(list(map(str, line)))}')
