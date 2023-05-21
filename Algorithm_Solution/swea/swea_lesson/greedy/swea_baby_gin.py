# baby-gin game

def perm(n,  k):
    global arrs
    if n == k:
        arrs += [list(map(int, p))]
    else:
        for i in range(k):
            if used[i] == 0:
                p[n] = arr[i]
                used[i] = 1
                perm(n+1, k)
                used[i] = 0


for tc in range(1, int(input())+1):
    arr = list(input())
    arrs = []
    p = [0] * 6
    used = [0] * 6
    perm(0, 6)

    for arr in arrs:
        triplet_cnt = run_cnt = 0
        if arr[0] == arr[1] == arr[2]:
            triplet_cnt += 1
        if arr[3] == arr[4] == arr[5]:
            triplet_cnt += 1
        if arr[0] + 1 == arr[1] == arr[2] - 1:
            run_cnt += 1
        if arr[3] + 1 == arr[4] == arr[5] - 1:
            run_cnt += 1

        if triplet_cnt == run_cnt == 1 or triplet_cnt == 2 or run_cnt == 2:
            print(f'#{tc} Baby Gin')
            break
    else:
        print(f'#{tc} Lose')