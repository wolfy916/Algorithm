# 숨바꼭질 2
# bfs 풀이

N, K = map(int, input().split())
visited = [0] * 100001

delta = [-1, 1, 0]
q = [N]
visited[N] = 1
cnt = 0
while q:
    v = q.pop(0)
    # 기록된 최소시간보다 긴 시간을 갖고있다면 pass
    if visited[K] != 0 and visited[v] > visited[K]:
        continue
    # 최소시간에 도착한 경우 += 1
    if v == K:
        cnt += 1
    else:
        delta[2] = v
        for d in delta:
            w = v + d
            # 유효성 인덱스 검사 + 방문하지 않았거나 이번 방문이 더 적게 걸린 시간일 경우
            if 0 <= w <= 100000 and (not visited[w] or visited[v] < visited[w]):
                visited[w] = visited[v] + 1
                q.append(w)

print(visited[K] - 1)
print(cnt)