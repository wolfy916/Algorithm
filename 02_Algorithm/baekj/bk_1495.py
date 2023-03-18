# 기타리스트

def dfs(pre_s, idx):  # (이전 사운드, 현재 곡 인덱스)
    global result
    # 마지막 곡의 볼륨으로 갱신
    if idx == N:
        result = max(result, pre_s)
        return True
    else:
        check = False  # 사운드의 유효성을 체크
        sounds = [pre_s-V[idx], pre_s+V[idx]]  # 두가지 볼륨 계산
        # 유효한 값인지 체크
        for cur_s in sounds:
            if 0 <= cur_s <= M and possible[idx+1][cur_s]:
                check = True
                # 다음 곡의 볼륨에서 재귀를 모두 실패했다면
                if dfs(cur_s, idx+1):
                    # 현재 재귀 경로는 실패하는 경로임을 기록
                    possible[idx+1][cur_s] = False

        # 볼륨들이 모두 유효하지 않다면 return False
        return True if check else False


# input
N, S, M = map(int, input().split())  # 1 ≤ N ≤ 50, 1 ≤ M ≤ 1,000, 0 ≤ S ≤ M
V = list(map(int, input().split()))  # 0 <= V[i] <= M

# 2차원 visited
# row: 곡 인덱스, col: 가능한 사운드값
possible = [[True for _ in range(M+1)] for _ in range(N+1)]

result = -1
dfs(S, 0)
print(result)