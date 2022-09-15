# 5178. 노드의 합 (제출용)
def post_order(i):
    if i <= N:
        post_order(2*i)
        post_order(2*i+1)
        if 2*i <= N:
            line[i] += line[2*i]
        if 2*i+1 <= N:
            line[i] += line[2*i+1]
        if 2*i > N and 2*i+1 > N:
            line[i] = values[leaf_nums.index(i)]


for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    leaf_num_and_value = [list(map(int, input().split())) for _ in '_' * M]

    leaf_nums = []
    values = []
    for leaf, value in leaf_num_and_value:
        leaf_nums += [leaf]
        values += [value]
    line = [0] * (N + 1)
    post_order(1)

    print(f'#{tc} {line[L]}')