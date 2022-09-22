info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

info2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]


answer = 1
wolf = 0

chd = [[] for _ in '_'*(len(info2))]
par = [0]*(len(info2))
for p, c in edges2:
    chd[p].append(c)
    par[c] = p
print('------------------------------------------------------------------------------')
print(f'간선정보 : {chd}')
print(f'부모 노드 정보 : {par}')
print(f'양, 늑대 정보 : {info2}')
print('------------------------------------------------------------------------------')

q = chd[0]
q.sort(key=lambda x: info2[x])
print(f'시작 큐 : {q}')
while q:
    v = q.pop(0)
    if info2[v] == 0:
        answer += 1
        for x in chd[v]:
            par[x] = par[v]
        chd[par[v]] += chd[v]
        chd[v].clear()
    elif info2[v] == 1:
        wolf += 1
        if answer - wolf == 0:
            wolf -= 1
            if len(q) != 0:
                q.append(v)
        elif not chd[v]:
            wolf -= 1
        else:
            for x in chd[v]:
                par[x] = par[v]
            chd[par[v]] += chd[v]
            chd[v].clear()
    q.sort(key=lambda x: info2[x])
    check_only_wolf = 1
    for w in q:
        if info2[w] == 0:
            check_only_wolf = 0
            break
    if check_only_wolf:
        for w in q:
            if chd[w]:
                break
        else:
            break
        q.sort(key=lambda x: len(chd[x]), reverse=True)
        check_len = 1
        for i in range(len(q)-1):
            if len(chd[q[i]]) != len(chd[q[i+1]]):
                check_len = 0
        if check_len:
            q.sort(key=lambda x: info2[chd[x][0]])

    print('------------------------------------------------------------------------------')
    print(f'간선정보 : {chd}')
    print(f'부모 노드 정보 : {par}')
    print(f'양, 늑대 정보 : {info2}')
    print(f'큐 : {q}')
    print(f'현재 양 : {answer}')
    print(f'현재 늑대 : {wolf}')
    print('------------------------------------------------------------------------------')
print(answer)