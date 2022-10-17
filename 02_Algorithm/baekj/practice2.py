T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))

    heights.sort()        # 오름차순 정렬
    top = heights[-1]     # top 할당
    differs = []          # 차이값을 담은 리스트
    cnt = 0               # 차이값이 홀수인 숫자들의 갯수
    for height in heights:
        differ = top - height
        differs.append(differ)
        if differ % 2:
            cnt += 1

    day = 0  # 출력값
    while differs.count(0) != N:  # 차이값이 모두 0이 되면 종료
        day += 1

        # 홀수 날
        if day % 2:
            for i in range(N-1):  # 차이값이 가장 큰녀석 부터 탐색

                # 차이값 0이면
                if not differs[i]:
                    continue

                # 차이값이 홀수이면
                elif differs[i] % 2:
                    differs[i] -= 1
                    cnt -= 1  # 차이값이 홀수인 cnt 값 -1
                    break

                # 차이값이 홀수인 녀석들이 없고, 총 차이값의 합이 2보다 크며, 해당 차이값이 짝수일 때
                elif not cnt and sum(differs) > 2 and not differs[i] % 2:
                    differs[i] -= 1
                    cnt += 1  # 홀수가 늘어남
                    break

        # 짝수 날
        else:
            for i in range(N-1):  # 차이값이 가장 큰녀석 부터 탐색

                # 차이값 0이면 패스 ~
                if not differs[i]:
                    continue

                # 차이값이 1보다 크면~
                elif differs > 1:
                    differs[i] -= 2
                    break

    print(f'#{tc} {day}')