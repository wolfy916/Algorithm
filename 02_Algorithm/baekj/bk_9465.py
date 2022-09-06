# 스티커

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    sticker_arr = [list(map(int, input().split())) for _ in '_'*2]

    if n >= 2:  # n이 2이상일 때, j == 1에 각각의 대각 합 할당
        sticker_arr[1][1] += sticker_arr[0][0]
        sticker_arr[0][1] += sticker_arr[1][0]

    i = 2
    while i != n and n != 1:  # 1단계 전 합 vs 2단계 전 합 <- 큰 값을 사용하여 합산 후 할당 <- 지그 재그에서 건너뛴 녀석에 대한 탐색이 가능함
        if sticker_arr[1][i-1] >= sticker_arr[1][i-2]:
            sticker_arr[0][i] += sticker_arr[1][i-1]
        else:
            sticker_arr[0][i] += sticker_arr[1][i-2]

        if sticker_arr[0][i-1] >= sticker_arr[0][i-2]:
            sticker_arr[1][i] += sticker_arr[0][i-1]
        else:
            sticker_arr[1][i] += sticker_arr[0][i-2]
        i += 1

    if sticker_arr[0][-1] >= sticker_arr[1][-1]:  # 마지막 인덱스까지 가서 위,아래 크기 비교
        result = sticker_arr[0][-1]
    else:
        result = sticker_arr[1][-1]

    print(result)  # 큰 값 출력
