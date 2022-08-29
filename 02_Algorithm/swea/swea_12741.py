# 두 전구

T = int(input())
result = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())  # A: X전구 켜진 시간, B+1: X전구 꺼진 시간, C: Y전구 켜진 시간, D+1: Y전구 꺼진 시간

    time = 0
    if B >= D:
        end_point = B
    else:
        end_point = D

    for i in range(end_point+1):
        if A < i <= B and C < i <= D:
            time += 1

    result += [time]

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')