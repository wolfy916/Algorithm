import sys

T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip('\n').split())
    print(A + B)