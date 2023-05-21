# 봉우리 찾기

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N: 지형의 갯수 (0 <= N <= 100)
    cnt = 0  # cnt : 봉우리 카운트
    if N:
        arr = [0] + list(map(int, input().split())) + [0]  # arr: 지형의 높이를 원소로 갖는 리스트(0<=높이<=10)
        hill = []  # hill: 높이값을 추가하여 봉우리인지 테스트할 리스트
        check = 0
        for i in range(0, N+2):
            if not hill:            # hill이 비어있다면
                hill.append(arr[i]) # append
            else:
                if hill[-1] <= arr[i]:   # 비교 높이가 hill 마지막 원소값 이상이라면
                    hill.append(arr[i])  # append
                    check = 0
                elif hill[-1] > arr[i] and not check:  # 비교 높이가 hill 마지막 원소값 미만이라면
                    hill.clear()
                    cnt += 1             # 언덕 1개 카운트
                    check = 1
                    hill.append(arr[i])
                elif hill[-1] > arr[i] and check:
                    hill.append(arr[i])

    print(f'#{tc} {cnt}')