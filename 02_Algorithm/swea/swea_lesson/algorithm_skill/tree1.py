# 트리 구조
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def pre(n):
    global cnt
    if n:
        cnt += 1
        print(n, end=' ')
        pre(ch1[n])
        pre(ch2[n])


def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


V = int(input())  # 노드수
arr = list(map(int, input().split()))
E = V - 1           # 간선수
ch1 = [0] * (V+1)   # 부모 인덱스, 자식 번호 저장
ch2 = [0] * (V+1)
par = [0] * (V+1)   # 자식 인덱스, 부모 번호 저장

# 부모 인덱스, 자식 저장
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)
print(root)
cnt = 0
pre(root)
print()
print(cnt)
