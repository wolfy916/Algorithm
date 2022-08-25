T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    line = list(map(int, input().split()))

    front = 0
    rear = N-1
    for _ in range(M):
        front += 1  # 디큐
        front %= N  # 인덱스 초과 -> 큐의 크기만큼으로 나머지 연산
        rear += 1  # 인큐
        rear %= N  # 인덱스 초과 -> 큐의 크기만큼으로 나머지 연산

    print(f'#{tc} {line[front]}')