t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ab_inform = [tuple(map(int, input().split())) for _ in range(n)]  # [a_i, b_i]를 원소로 리스트 할당
    p = int(input())
    c = [int(input()) for _ in range(p)]

    bus_path = [0] * 5000  # 각 정류장의 노선 개수를 리스트 할당
    for x, y in ab_inform:
        for k in range(x-1, y):  # 정류장 번호가 A_i <= x <= B_i
            bus_path[k] += 1

    print(f'#{tc}', end=' ')  # 출력 구문
    for num in c:
        print(f'{bus_path[num-1]}', end=' ')
    print()