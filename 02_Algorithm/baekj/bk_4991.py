# 로봇청소기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

w, h = map(int, input().split())
robot = 'o'; clean = '.'; dirty = '*'; block = 'x'
dirty_num = 0
area = []
for i in range(h):
    line = list(input())
    for j in range(w):
        if line[j] == clean:
            continue
        elif line[j] == robot:
            si, sj = i, j
        elif line[j] == dirty:
            dirty_num += 1
    area.append(line)

area[si][sj] = clean
INF = 1000000
visited = [[[INF, dirty_num] for _ in '_'*w] for _ in '_'*h]
q = [(si, sj, dirty_num)]
visited[si][sj][0] = 0
result = -1
while q:
    vi, vj, d = q.pop(0)
    if not d:
        result = visited[vi][vj][0]
        break
    else:
        for di, dj in delta:
            wi, wj = vi+di, vj+dj
            if 0 <= wi < h and 0 <= wj < w:
                if visited[wi][wj][0] >= visited[vi][vj][0]:
                    if visited[wi][wj][1] >= visited[vi][vj][1]:
                        if area[wi][wj] == clean:
                            visited[wi][wj][0] = visited[vi][vj][0] + 1
                            if area[wi][wj] == dirty:
                                area[wi][wj] = clean
                                d -= 1
                            visited[wi][wj][1] = d
                            q.append((wi, wj, d))
print(result)