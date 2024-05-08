# 압축
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] dfs
def dfs(idx):
    value, i = 0, idx
    while i < len(S):
        if S[i] == '(':
            v, n = dfs(i+1)
            value += int(S[i-1]) * v - 1
            i = n
        elif S[i] == ')':
            return value, i
        else:
            value += 1
        i += 1
    return value, i

# [main]
if __name__ == '__main__':
    S = input()
    print(dfs(0)[0])