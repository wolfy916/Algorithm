import sys

N = int(input())
inputV = list(map(int, sys.stdin.readline().split()))
print(min(inputV), max(inputV))