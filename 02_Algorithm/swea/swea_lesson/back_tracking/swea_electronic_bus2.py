# 10956. 5208. [구현] 5일차 - 전기버스2 (제출용)
def back_tracking(i, n, c, e):
    global cnt
    if i == n:
        if cnt > c:
            cnt = c
    elif c >= cnt:  # 이미 기존의 최소 교환 횟수만큼 교환한 경우
        return
    else:
        back_tracking(i+1, n, c+1, arr[i]-1)  # 교체하고, 다음 정류장으로 이동
        if e > 0:  # 배터리가 남아있으면
            back_tracking(i+1, n, c, e-1)  # 교체하지 않고, 다음 정류장으로 이동


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = cnt = arr[0]  # 종점 포함 정류장 수
    # back_tracking(1, arr[0], 0, 0)  # 1번부터 고려하면 최종 교체 횟수에서 1번 제외
    back_tracking(2, arr[0], 0, arr[1]-1)  # 1번 정류장은 무조건 교체, 교체횟수에서 제외

    print(f'#{tc} {cnt}')