T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in '_'*N]

    result_cnt = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for di, dj in [[1,0], [-1,0], [1,1], [0,1], [-1,1], [1,-1], [0,-1], [-1,-1]]:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and area[i][j] > area[ni][nj]:
                    cnt += 1
            if cnt >= 4:
                result_cnt += 1

    print(f'#{tc} {result_cnt}')