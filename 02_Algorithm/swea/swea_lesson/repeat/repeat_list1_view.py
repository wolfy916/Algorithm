T = 10
for tc in range(1, T+1):
    N = int(input())
    area = list(map(int, input().split()))

    result = 0
    for i in range(2, N-2):
        a = area[i] - area[i-2]
        b = area[i] - area[i-1]
        c = area[i] - area[i+1]
        d = area[i] - area[i+2]
        line = [a, b, c, d]
        while True:
            cnt = 0
            for j in range(4):
                line[j] -= 1
            for x in line:
                if x < 0:
                    cnt += 1
            if cnt != 0:
                break
            result += 1

    print(f'#{tc} {result}')