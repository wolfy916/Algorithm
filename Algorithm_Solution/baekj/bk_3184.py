# 양
R, C = map(int, input().split())
area = [input() for _ in range(R)]
answer = [0, 0]
visited = [[False] * C for _ in range(R)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(R):
    for j in range(C):
        if visited[i][j]: continue
        if area[i][j] == '#' or area[i][j] == '.': continue
        visited[i][j] = True
        cnt = {'v': 0, 'o': 0}
        cnt[area[i][j]] += 1
        q = [(i, j)]
        while q:
            vi, vj = q.pop(0)
            for di, dj in delta:
                ni, nj = vi + di, vj + dj
                if ni < 0 or nj < 0 or ni >= R or nj >= C: continue
                if visited[ni][nj]: continue
                if area[ni][nj] == '#': continue
                if area[ni][nj] in cnt.keys():
                    cnt[area[ni][nj]] += 1
                visited[ni][nj] = True
                q.append((ni, nj))

        if cnt['v'] < cnt['o']:
            answer[0] += cnt['o']
        else:
            answer[1] += cnt['v']

print(*answer)