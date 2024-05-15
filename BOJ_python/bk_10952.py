import sys

while True:
    A, B = map(int, sys.stdin.readline().rstrip('\n').split())
    if A == 0 and B == 0:
        break
    print(A+B)