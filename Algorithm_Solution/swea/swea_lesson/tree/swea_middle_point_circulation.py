# 중위 순회
def in_order(n):
    global result
    if n:
        in_order(ch1[n])
        result += [n]
        in_order(ch2[n])


T = 10
for tc in range(1, T+1):
    V = int(input())  # 노드 갯수
    E = V - 1  # 간선 갯수
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    par = [0] * (V+1)
    string = [0] * (V+1)
    for i in range(V):
        arr = list(input().split())
        p = int(arr.pop(0))
        string[p] = arr.pop(0)

        while arr:
            c = int(arr.pop(0))
            if ch1[p] == 0:
                ch1[p] = c
            else:
                ch2[p] = c

    result = []
    in_order(1)

    print(f'#{tc} ', end='')
    for num in result:
        print(f'{string[num]}', end='')

    print()