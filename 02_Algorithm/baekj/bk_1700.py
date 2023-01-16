# 멀티탭 스케쥴링

# tap = 현재 콘센트 상황, idx = 사용할 전기용품의 인덱스, value = 콘센트를 뺀 횟수
def dfs(tap, idx, value):
    global result

    # 하나의 케이스라도 끝에 도달하여 result가 갱신되었을 때,
    # 그 갱신된 result보다 큰 값이라면 최소가 될 수 없는 경우이므로 컷
    if result != 1000 and result < value:
        return

    # 전기용품을 다 사용하여 끝에 도달하면 갱신 시도
    if idx == K:
        result = min(result, value)

    # 전기용품을 다 사용한 것이 아니라면
    else:
        # 사용하려는 전기용품이 tap에 꽂혀있다면 다음으로 pass
        if elecs[idx] in tap:
            dfs(tap, idx+1, value)

        # 꽃혀있지않은 새로운 전기용품이라면
        else:
            # tap에 빈 플러그 공간이 있다면
            if 0 in tap:
                empty_space = tap.index(0)
                tap[empty_space] = elecs[idx]
                dfs(tap, idx+1, value)

            # tap이 꽉 차있다면
            else:
                for i in range(N):
                    temp = tap[i]             #
                    tap[i] = elecs[idx]       #
                    dfs(tap, idx+1, value+1)  #
                    tap[i] = temp             # 백트랙킹


N, K = map(int, input().split())
elecs = list(map(int, input().split()))

# 콘센트의 크기가 전기용품 사용횟수보다 크다면 콘센트 뺄 일이 없으므로 0 종료
if N >= K:
    print(0)
    exit()

result = 1000  # 대충 INF 값
dfs([0]*N, 0, 0)
print(result)