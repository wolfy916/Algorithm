# 5177. [기본] 8일차 - 이진 힙 (제출용)
def node(i, s):
    if i <= N:
        tree[i] = num_list.pop(0)
        n = i
        while n != 0:
            if i > 1 and tree[n//2] > tree[n]:
                tree[n//2], tree[n] = tree[n], tree[n//2]
            n //= 2
        s = node(i+1, s)
    else:
        i -= 1
        while i != 0:
            i //= 2
            s += tree[i]
    return s


for tc in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    tree = [0] * (N+1)
    print(f'#{tc} {node(1, 0)}')