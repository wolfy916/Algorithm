# 구간 합 구하기

def create(s, e, node):
    if s == e:
        tree[node] = nums[s]
        return nums[s]
    mid = (s+e) // 2
    tree[node] = create(s, mid, node * 2) + create(mid+1, e, node * 2 + 1)
    return tree[node]


def sum_tree(s, e, node, left, right):
    if left > e or right < s:
        return 0
    if left <= s and e <= right:
        return tree[node]
    mid = (s + e) // 2
    return sum_tree(s, mid, node * 2, left, right) + sum_tree(mid + 1, e, node * 2 + 1, left, right)


def change(s, e, node, idx, dif):
    if idx < s or idx > e:
        return
    tree[node] += dif
    if s == e:
        return
    mid = (s + e) // 2
    change(s, mid, node * 2, idx, dif)
    change(mid + 1, e, node * 2 + 1, idx, dif)


N, M, K = map(int, input().split())
nums = [int(input()) for _ in '_'*N]
tree = [0] * (N*4)
create(0, N-1, 1)

for j in range(1, M+K+1):
    a, b, c = map(int, input().split())
    if a == 1:
        dif = nums[b-1] - c
        nums[b-1] = c
        change(0, N-1, 1, b-1, dif)
    else:
        print(sum_tree(0, N-1, 1, b-1, c-1))