# swea 2001. 파리 퇴치

# 5 <= N <= 15, 2 <= M <= N
# 각 영역의 파리수는 30 이하다.
# T = 테스트 케이스의 개수
# 최대한 많은 파리를 잡았을 때의 죽은 파리수는?


# 입력
# T
# N M
# N개(각 영역의 파리수) x N줄

def flapper():

    T = int(input())

    for i in range(T):

        N, M = map(int, input().split())
        area = []
        kill = []

        for m in range(N):
            area.append(list(map(int,input().split())))

        for o in range(N-M+1):
            for j in range(N-M+1):
                area_kill = []
                for k in range(M):
                    area_kill += area[k+o][j:j+M]
                kill.append(sum(area_kill))
            
        print(f'#{i+1} {max(kill)}')

flapper()
