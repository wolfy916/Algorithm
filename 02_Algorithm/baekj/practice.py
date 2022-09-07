# 쓰레기 수거
import sys
T = int(sys.stdin.readline())
for tc in range(T):
    W, N = map(int, sys.stdin.readline().split())
    road = [0]*(100001)    # 출발지(0)부터 마지막 지점까지의 길
    last_d = 0             # 마지막 지점의 거리
    for i in range(N):
        d, w = map(int, sys.stdin.readline().split())
        road[d] = w
        if i == N-1:
            last_d = d

    distance = 0           # 총 이동거리
    collect_w = 0          # 현재 수거한 쓰레기
    back = last_d          # 마지막에 수거하고 쓰레기장 복귀하는 길이
    for i in range(1, last_d+1):
        distance += 1
        if road[i] == 0:        # 쓰레기 없으면 패스
            pass
        else:                   # 쓰레기 있으면,
            if collect_w + road[i] <= W:    # 수거 가능하면
                collect_w += road[i]            # 담고
                road[i] = 0                     # 수거표시
                if collect_w == W:              # 용량 꽉찼으면 돌아가는데
                    if i == last_d:             # 마지막 지점이면 그대로 종료
                        break
                    else:
                        distance += i+i         # 마지막 지점 아니면 쓰레기장가서 비우고 돌아옴
                        collect_w = 0
            else:                           # 수거 불가능하면
                distance += i+i                 # 쓰레기장가서 비우고 돌아와서 담음
                collect_w = road[i]

    print(distance+back)