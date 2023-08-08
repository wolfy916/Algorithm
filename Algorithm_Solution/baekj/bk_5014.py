# 스타트 링크
# bfs 풀이

# [1] 입력과 초기화
total, start, goal, up, down = map(int, input().split())
btns = []  # up, down 버튼
if up != 0: btns.append(up)      # up, down 값이 0이라면 순회할 필요도 없음
if down != 0: btns.append(-down) #
visited = [0] * (total + 1)      # visited[n] - 1 = n층을 가기위한 최소한의 버튼 클릭수
visited[start] = 1
q = [start]
answer = "use the stairs"

# [2] queue를 이용한 bfs
while q:
    v = q.pop(0)
    if v == goal:
        answer = visited[goal] - 1
        break

    for btn in btns:
        w = v + btn
        if 0 < w < total + 1 and not visited[w]:
            visited[w] = visited[v] + 1
            q.append(w)

print(answer)