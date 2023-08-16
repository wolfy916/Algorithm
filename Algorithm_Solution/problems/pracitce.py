# 소트게임
# dfs로는 뭔가 답이 잘안나오나?
import sys
sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline().rstrip('\n')

N, K = map(int, input().split())
nums = list(map(int, input().split()))

def dfs(select, cur):
    global answer
    if answer > 0: return
    if select != [] and cur == nums: return
    if cur == sorted_nums:
        answer = len(set(select))
        return
    for i in range(N - K + 1):
        temp = cur[:]
        if K > 1:
            for j in range(K // 2):
                temp[i + j], temp[i + K - j - 1] = temp[i + K - j - 1], temp[i + j]
        key = ''.join(map(str, temp))
        if not visited.get(key):
            visited[key] = True
            dfs(select + [nums[i]], temp)

sorted_nums = sorted(nums)
answer = -1
visited = dict()
dfs([], nums)
print(answer)