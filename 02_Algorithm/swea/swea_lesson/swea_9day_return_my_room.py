T = int(input())
for tc in range(1, T+1):
    N = int(input())
    move = [tuple(map(int, input().split())) for _ in '_' * N]

    path = [0] * 401  # 경로 확인용 zero 리스트 생성
    for start, end in move:  # 시작 방 번호와 도착 방 번호를 하나씩 꺼내기

        if start > end:  # 시작 방번호가 더 클 경우, 상호 교환
            start, end = end, start

        if start % 2 and not end % 2:  # 방 번호가 홀 짝인 경우
            if end - start == 1:  # 방 번호의 차이값이 1인 경우
                path[start] += 1
                path[end] += 1
            else:
                for l in range(start, end + 1):
                    path[l] += 1

        elif not start % 2 and end % 2:  # 방 번호가 짝 홀인 경우
            for i in range(start - 1, end + 2):
                path[i] += 1

        elif start % 2 and end % 2:  # 방 번호가 홀 홀일 경우
            for j in range(start, end + 2):
                path[j] += 1

        else:  # 방 번호가 짝 짝일 경우
            for k in range(start - 1, end + 1):
                path[k] += 1

    time = 0
    for x in path:  # 가장 높은 숫자를 time에 할당
        if time < x:
            time = x

    print(f'#{tc} {time}')