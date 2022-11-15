# 빵집

# input
R, C = map(int, input().split())
area = [['x']*(C+2)] + [['x'] + list(input()) + ['x'] for _ in '_'*R] + [['x']*(C+2)]

visited = [[0]*(C+2) for _ in '_'*(R+2)]  # visited
delta = [(-1, 1), (0, 1), (1, 1)]  # 우측상단, 우측, 우측하단
arrives = [0] * (R+1)  # n번째 파이프의 최종 연결 여부


def dfs(vi, vj, s):  # (vi, vj) 와 s: 파이프 번호
    global maxV

    if vj == C:  # 파이프가 마지막 열 인덱스에 도착하여 연결 성공
        arrives[s] = 1  # 해당 파이프가 연결됨을  기록
        maxV += 1

    for di, dj in delta:
        ni, nj = vi+di, vj+dj
        # 유효 인덱스검사 and not visited
        if area[ni][nj] != 'x' and not visited[ni][nj]:
            visited[ni][nj] = s  # visited
            dfs(ni, nj, s)

            # 해당 파이프가 연결에 성공했다면 무차별 리턴
            if arrives[s]:
                return
            # visited[ni][nj] = 0  -> 시간초과 나게 만든 뻘 짓

maxV = 0
for i in range(1, R+1):
    dfs(i, 1, i)  # 파이프 하나씩 연결하러 출발

print(maxV)