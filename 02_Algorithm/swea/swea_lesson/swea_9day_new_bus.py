t = int(input())
for tc in range(1, t+1):
    n = int(input())
    bus_inform = [list(map(int, input().split())) for _ in '_' * n]

    bus_path = [0] * 1001  # 각 정류장의 노선 개수를 리스트 할당
    for x, y, z in bus_inform:
        if x == 1:  # 일반 버스
            for i in range(y, z + 1):
                bus_path[i] += 1
        elif x == 2:  # 급행 버스
            for j in range(y, z + 1, 2):
                bus_path[j] += 1
        else:  # 광역 급행 버스
            if y % 2:
                for k in range(y, z + 1):
                    if k % 3 == 0 and k % 10 != 0:
                        bus_path[k] += 1
            else:
                for l in range(y, z + 1):
                    if l % 4 == 0:
                        bus_path[l] += 1

    maxV = 0
    for v in bus_path:
        if maxV < v:
            maxV = v

    print(f'#{tc} {maxV}')