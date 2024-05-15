T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())  # D : 기차 전면부 사이 거리, A : A기차 속력, B : B기차 속력, F : 파리의 속력

    i = 1
    fly_s = 0
    while D > 10**(-6):
        if i % 2:
            hour = D/(F+B)
            fly_s += F * hour
            D = (F-A) * hour
        else:
            hour = D/(F+A)
            fly_s += F * hour
            D = (F-B) * hour

        i += 1

    print(f'#{tc} {fly_s}')

# T = int(input())
# for tc in range(1, T + 1):
#     D, A, B, F = map(int, input().split())
#
#     hour = D / (A + B)
#     fly_s = F * hour
#
#     print(f'#{tc} {fly_s}')