# 좋은 수열
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 좋은 수열 판별
def check(v):
    if len(v) == 1: return True
    lenV = 0
    for i in range(len(v) - 1, len(v) // 2 - 1, -1):
        lenV += 1
        if v[i - lenV: i] == v[i:]:
            return False
    return True

# [C] 백트랙킹 함수
def dfs(v):
    global answer
    if len(v) == N:
        answer = v
        return
    for n in '123':
        if check(v + n):
            dfs(v + n)
        if answer: return

# [main]
if __name__ == '__main__':
    N = int(input())
    answer = ''
    dfs('')
    print(answer)