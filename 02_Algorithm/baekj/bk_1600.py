# 말이 되고픈 원숭이
# W와 H는 1이상 200이하의 자연수이고, K는 0이상 30이하의 정수

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(vi, vj, k, v, lst):
    global result

    if (vi, vj) == (W - 1, H - 1):
        if k > K:
            result = min(result, v - K * 3)
        else:
            result = min(result, v - k * 3)
    else:
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if 0 <= ni < H and 0 <= nj < W:
                if not area[ni][nj] or area[vi][vj] < area[ni][nj]:
                    area[ni][nj] = v + 1
                    if len(lst) == 3:
                        if abs(lst[0][0] - ni) + abs(lst[0][1] - nj) == 3:
                            dfs(ni, nj, k + 1, v + 1, lst[1:] + [(ni, nj)])
                        else:
                            dfs(ni, nj, k, v + 1, lst[1:] + [(ni, nj)])
                    else:
                        dfs(ni, nj, k, v + 1, lst + [(ni, nj)])

K = int(input())
W, H = map(int, input().split())
area = [list(map(int, input().split())) for _ in '_'*H]
result = W * H + 1
area[0][0] = 1
dfs(0, 0, 0, 1, [(0, 0)])
if result == W * H + 1:
    print(-1)
else:
    print(result)