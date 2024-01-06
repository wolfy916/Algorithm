import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] carry 여부 체크 함수
def check(num1, num2):
    div = 100000000
    while div > 0:
        value1 = num1 // div
        value2 = num2 // div
        if value1 and value2:
            if value1 + value2 > 9:
                return False
        if value1:
            num1 -= value1 * div
        if value2:
            num2 -= value2 * div
        div //= 10
    return True 

# [C] 백트랙킹 함수
def dfs(depth, start, value):
    global answer, is_checked
    if selects in is_checked: return
    if len(selects):
        is_checked.append(selects.copy())
    answer = max(answer, depth)
    for i in range(start, N):
        if is_selected[i]: continue
        if check(value, nums[i]):
            selects.add(i)
            is_selected[i] = True
            dfs(depth + 1, start + 1, value + nums[i])
            selects.remove(i)
            is_selected[i] = False

# [Main]
if __name__ == "__main__":
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    is_checked = []
    selects = set()
    is_selected = [False] * N
    answer = 0
    dfs(0, 0, 0)
    print(answer)