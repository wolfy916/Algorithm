# Dance Dance Revolution
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(left, right, sumV, i):
    global result
    temp = DDR[i]

    if not temp:
        result = min(result, sumV)
    else:
        if left and right != temp:
            if visited[i] and visited[i] <= sumV + cost[abs(left - temp)]:
                return
            else:
                visited[i] = sumV + cost[abs(left - temp)]
            dfs(temp, right, sumV + cost[abs(left - temp)], i + 1)
        else:
            dfs(temp, right, sumV + 2, i + 1)

        if right and left != temp:
            if visited[i] and visited[i] <= sumV + cost[abs(right - temp)]:
                return
            else:
                visited[i] = sumV + cost[abs(right - temp)]
            dfs(left, temp, sumV + cost[abs(right - temp)], i + 1)
        else:
            dfs(left, temp, sumV + 2, i + 1)


DDR = list(map(int, input().split()))
cost = [1, 3, 4, 3]
visited = [0] * 100001
result = 400000
dfs(0, 0, 0, 0)
print(result)