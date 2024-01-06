from itertools import product

a, b = map(int, input().split())
x, y = len(str(a)), len(str(b))

cnt = 0

for i in range(x, y+1):
    lst = list(product([4, 7], repeat=i))
    for num in lst:
        n = int(''.join(map(str, num)))
        if a <= n <= b:
            cnt += 1

print(cnt)