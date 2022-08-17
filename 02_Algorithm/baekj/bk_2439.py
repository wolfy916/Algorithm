import sys

N = int(sys.stdin.readline().rstrip('\n'))
for i in range(N):
    print(' '*(N-i-1) + '*'*(i+1))