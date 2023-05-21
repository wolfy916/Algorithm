# 세제곱근을 찾아라

for tc in range(1, int(input()) + 1):
    N = input()

    i = (len(N)-1)//3
    N = int(N)

    for num in range(10**i, 10**(i+1)):
        if num**3 == N:
            print(f'#{tc} {num}')
            break
    else:
        print(f'#{tc} -1')