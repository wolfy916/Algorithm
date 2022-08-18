a, b = map(int, input().split())

G = 1
L = 0
big_num = 0

if a > b:
    big_num = a
elif a < b:
    big_num = b

if big_num != 0:
    for x in range(1, big_num + 1):
        if a % x == 0 and b % x == 0:
            if G < x:
                G = x
    n = big_num
    while True:
        if n % a == 0 and n % b == 0:
            break
        n += big_num
    L = n
else:
    G = a
    L = a

print(G)
print(L)