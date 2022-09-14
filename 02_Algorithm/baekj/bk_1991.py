# 트리 순회
def pre(n):
    if n:
        print(chr(n+64), end='')
        pre(ch1[n])
        pre(ch2[n])


def in_order(n):
    if n:
        in_order(ch1[n])
        print(chr(n+64), end='')
        in_order(ch2[n])


def post_order(n):
    if n:
        post_order(ch1[n])
        post_order(ch2[n])
        print(chr(n+64), end='')


V = int(input())
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
for _ in '_' * V:
    arr = list(input().split())
    p = ord(arr[0]) - 64
    if arr[1] != '.':
        ch1[p] = ord(arr[1]) - 64
    if arr[2] != '.':
        ch2[p] = ord(arr[2]) - 64

pre(1)
print()
in_order(1)
print()
post_order(1)