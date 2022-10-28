# 로봇청소기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(vi, vj):


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

print(result)