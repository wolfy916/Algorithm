# 양팔 저울

from sys import stdin
input = stdin.readline

N = int(input())  # 1 <= 추의 개수 <= 30
arr_N = list(map(int, input().split()))  # 1g <= 추의 무게 <= 500g
M = int(input())  # 1 <= 구슬의 개수 <= 7
arr_M = list(map(int, input().split()))  # 1g <= 구슬의 무게 <= 40,000g

