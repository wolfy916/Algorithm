T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())  # K : 충전 한 번에 이동가능한 거리, N : 버스 정류장 수, M : 충전기가 있는 정류장 수
    charge_station = list(map(int, input().split()))  # 충전기가 있는 정류장 번호 리스트

    bus = 0
    result = 0
    while bus + K < N:
        for x in reversed(charge_station):
            if bus < x <= bus + K:
                bus = x
                result += 1
                break
        else:
            result = 0
            break

    print(f'#{tc} {result}')



