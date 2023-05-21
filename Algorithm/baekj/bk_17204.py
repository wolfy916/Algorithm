# 죽음의 게임

N, K = map(int, input().split())
arr = [int(input()) for _ in '_' * N]

visited = [0] * N  # visited
turn = 0           # 현재 차례인 사람의 번호, 초기값 : 영기번호
cnt = 0
while turn != K:            # 종료조건 1. 보성이가 지목되면 종료
    cnt += 1

    if arr[turn] == turn:   # 종료조건 2. 자기 자신을 지목할 경우 종료
        cnt = -1
        break

    if visited[turn] == 1:  # 종료조건 3. 무한하게 순환할 경우 종료
        cnt = -1
        break

    visited[turn] = 1
    turn = arr[turn]        # 현재 차례가 다음 번호 지목

print(cnt)