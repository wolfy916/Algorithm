# 5176. [기본] 8일차 - 이진탐색 (제출용)
def in_order(i):
    if i <= N:
        in_order(2*i)
        line[i] = num_list.pop(0)
        in_order(2*i+1)


for tc in range(1, int(input())+1):
    N = int(input())
    num_list = list(range(1, N+1))
    line = [0] * (N + 1)
    in_order(1)

    print(f'#{tc} {line[1]} {line[N//2]}')