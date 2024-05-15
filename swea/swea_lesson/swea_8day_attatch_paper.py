# stack 실습 종이 붙이기

# 10x20, 20x20인 직사각형 종이
# 10≤N≤300, N은 10의 배수

def AhAhAhAh_fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    else:
        return AhAhAhAh_fibo(n-1) + AhAhAhAh_fibo(n-2) * 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {AhAhAhAh_fibo(N//10)}')