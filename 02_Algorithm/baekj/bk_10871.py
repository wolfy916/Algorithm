import sys

N, X = map(int, sys.stdin.readline().rstrip('\n').split())
A = list(map(int, sys.stdin.readline().rstrip('\n').split()))

test_list = []
for i in range(N):
    if X > A[i]:
        test_list += [A[i]]
print(' '.join(list(map(str, test_list))))