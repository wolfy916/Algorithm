# 어디에 들어갈 수 있을까?

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]   # 2차원 배열 생성

    cnt = 0
    for i in range(N):
        test_list = []
        for j in range(N):
            test_list += [area[i][j]]
            if test_list[0] == 0 or test_list[-1] == 0:
                test_list = []
                continue
            if len(test_list) > K:
                test_list = []
                continue
            if len(test_list) == K and (j == N-1 or area[i][j+1] == 0):
                cnt += 1
                test_list = []

    for i in range(N):
        test_list = []
        for j in range(N):
            test_list += [area[j][i]]
            if test_list[0] == 0 or test_list[-1] == 0:
                test_list = []
            if len(test_list) > K:
                test_list = []
            if len(test_list) == K and (j == N-1 or area[j+1][i] == 0):
                cnt += 1
                test_list = []

    print(f'#{tc} {cnt}')