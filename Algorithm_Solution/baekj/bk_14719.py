H, W = map(int, input().split())
area = list(map(int, input().split()))

sumV = 0
iter_cnt = 0
while iter_cnt < H:

    # 좌측부터 이어져 있는 0과 음수 탐색
    left_cnt = 0
    for i in range(len(area)):
        if area[i] <= 0:
            zero_left_index = i
            left_cnt += 1
        else:
            break

    # 우측부터 이어져 있는 0과 음수 탐색
    right_cnt = 0
    for j in range(len(area)-1 , -1, -1):
        if area[j] <= 0:
            zero_right_index = j
            right_cnt += 1
        else:
            break

    # 탐색한 결과대로 슬라이싱하여 제외
    if left_cnt == 0 and right_cnt == 0:
        pass
    elif left_cnt != 0 and right_cnt == 0:
        area = area[zero_left_index+1:]
    elif left_cnt == 0 and right_cnt != 0:
        area = area[:zero_right_index]
    elif left_cnt != 0 and right_cnt != 0:
        area = area[zero_left_index+1:zero_right_index]

    # 0과 음수의 수를 세어 sumV에 더하고, 1씩 빼기
    for k in range(len(area)):
        if area[k] <= 0:
            sumV += 1
        area[k] -= 1

    iter_cnt += 1

print(sumV)