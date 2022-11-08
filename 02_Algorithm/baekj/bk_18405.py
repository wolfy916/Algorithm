# 경쟁적 전염

'''
첫번째 시도 (5% 시간초과)
	-> queue 1개 사용, while문 2중첩, for문 2중첩으로 append, lambda 사용
두번째 시도 (22% 시간초과)
	-> queue 1개 사용, while문 2중첩, used로 check 후 append, lambda 사용
'''

N, K = map(int, input().split())
area = [['-'] * (N + 2)] + [['-'] + list(map(int, input().split())) + ['-'] for _ in '_' * N] + [['-'] * (N + 2)]
S, X, Y = map(int, input().split())

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# q1 초기값 <- 모든 바이러스들 (i, j, 종류번호) append
q1 = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if area[i][j]:
            q1.append((i, j, area[i][j]))

time = 0
while time < S:  # 시간되면 종료

    # 단위 시간당 사건 제어를 위해 queue 를 2개 사용
    q1.sort(key=lambda x: x[2])  # q1 바이러스 종류번호 기준 오름차순 정렬
    q2 = q1[:]  # q1을 복사해서 q2에 할당
    q1.clear()  # q1의 모든 원소 삭제

    while q2:  # q2가 모두 소진되면 단위 시간 사건이 종료된 것
        vi, vj, k = q2.pop(0)
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            # 인덱스 유효성 검사 and 바이러스가 없는 곳인지 확인
            if area[ni][nj] != '-' and not area[ni][nj]:
                area[ni][nj] = k  # 바이러스 증식
                q1.append((ni, nj, k))  # q1에 append

    time += 1  # 단위 시간 증가

print(area[X][Y])