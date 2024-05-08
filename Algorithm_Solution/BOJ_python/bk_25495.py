# 에어팟

N = int(input())                     # 에어팟 연결 횟수
A = list(map(int, input().split()))  # 에어팟에 연결을 시도한 핸드폰 리스트

battery_consumption = 2
using_phone = A[0]
repeat_cnt = 1
for phone in A[1:]:
    if using_phone == phone:
        repeat_cnt += 1
        battery_consumption += 2 ** repeat_cnt
    else:
        repeat_cnt = 1
        using_phone = phone
        battery_consumption += 2

    if battery_consumption >= 100:
        repeat_cnt = 0
        battery_consumption = 0

print(battery_consumption)

