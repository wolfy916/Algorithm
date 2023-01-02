# 여행 가자

def bfs(idx):
    # idx는 plans의 인덱스
    s, e = plans[idx], plans[idx+1]
    visited = [0] * (N+1)
    q = [s]
    visited[s] = 1
    while q:
        v = q.pop(0)
        # 목적지 도착
        if v == e:
            # 최종목적지인지 확인
            if idx + 1 == M - 1:
                return True
            else:
                # 다음 목적지로 이동
                if bfs(idx + 1):
                    return True
        else:
            # bfs, queue
            for w in range(1, N+1):
                if adjM[v][w] and not visited[w]:
                    visited[w] = 1
                    q.append(w)
    # s -> e 경로 없음
    return False

N, M = int(input()), int(input())  # N <= 200, M <= 1000
adjM = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in '_'*N]
plans = list(map(int, input().split()))

if bfs(0):
    print("YES")
else:
    print("NO")
