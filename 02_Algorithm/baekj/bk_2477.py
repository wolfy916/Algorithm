# 참외밭

K = int(input())  # 참외 개수
arr = [list(map(int, input().split())) for _ in '_' * 6]

double_arr = arr * 2
STACK = []
for i in range(11):
    STACK += [double_arr[i]]
    if len(STACK) == 4 and STACK[0][0] == STACK[2][0] and STACK[1][0] == STACK[3][0]:
        small_area = STACK[1][1] * STACK[2][1]
        break
    if len(STACK) == 4:
        STACK.pop(0)

big_area = []
for j in range(6):
    if arr[j] not in STACK:
        big_area += [arr[j][1]]

result = ((big_area[0] * big_area[1]) - small_area) * K

print(result)