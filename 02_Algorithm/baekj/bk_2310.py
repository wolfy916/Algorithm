# 어드벤처 게임

def bfs(n):
    visited = [0]*(n+1)
    q = [(1, 0)]  # 1번 방에 0골드를 들고 있는 상태
    while q:
        v, gold = q.pop(0)

        # 방 도착
        if v == n:
            # n번 방에 트롤이 있을 경우
            if maze[v][0] == 'T':
                # 돈이 있어야 Yes로 종료
                if gold >= maze[v][1]:
                    print('Yes')
                    return
            else:
                # n번 방에 트롤이 없을 경우
                print('Yes')  # Yes로 종료
                return
        else:
            # 돈 채워주는 방
            if maze[v][0] == 'L':
                gold = max(gold, maze[v][1])

            # 삥 뜯기는 방
            elif maze[v][0] == 'T':
                if gold >= maze[v][1]:
                    gold -= maze[v][1]

            for w in maze[v][2:]:
                if w:
                    # 방문하지 않았거나, 전에 방문했을 때보다 돈이 더 많을 때
                    if not visited[w] or visited[w] < gold:
                        visited[w] = gold
                        q.append((w, gold))
    # 다 돌면 No로 종료
    print('No')
    return


while True:
    n = int(input())
    if not n:
        break
    maze = [[0]]
    for _ in '_'*n:
        char, *info = input().split()
        maze.append([char]+list(map(int, info)))
    bfs(n)