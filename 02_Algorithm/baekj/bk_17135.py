# 캐슬 디펜스
import sys
input = sys.stdin.readline

N, M, D = map(int, input().split())
area = [list(map(int, input().split())) for _ in '_'*N]

priority = [0] * M

for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            priority[j] += 1
            for k in range(1, M):
                if 0 <= j+k < M:
                    priority[j+k] += k+1
                if 0 <= j-k < M:
                    priority[j-k] += k+1

print(priority)