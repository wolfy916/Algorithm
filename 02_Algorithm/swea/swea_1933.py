# 간단한 N의 약수
# 1 <= N <= 1,000
# N은 정수

N = int(input())
for i in range(1,N+1):
    if N % i == 0:
        print(f'{i} ', end='')