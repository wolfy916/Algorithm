# 크리스마스 트리(N -> 1방향)
# 1 <= N <= 10, 0 <= color <= 100

# [A] 팩토리얼 함수
def fa(n):
    if n == 1:
        return 1
    return n * fa(n - 1)


# [B] k레벨에서 현재 갖고 있는 r, g, b로 가능한 경우의 수를 cnt에 기록하여 리턴하는 재귀함수
def dfs(k, r, g, b):

    # 경우의 수를 기록할 변수 선언 및 초기화
    cnt = 0

    # 1레벨 도달시 마지막 1칸을 채우며 종료하는 조건
    if k == 1:
        if r: cnt += 1
        if g: cnt += 1
        if b: cnt += 1
        return cnt

    # 레벨을 하나의 색으로 채우고 이전 레벨로 재귀
    if r >= k:
        cnt += dfs(k - 1, r - k, g, b)
    if g >= k:
        cnt += dfs(k - 1, r, g - k, b)
    if b >= k:
        cnt += dfs(k - 1, r, g, b - k)

    # 레벨을 두가지 색으로 채우고 이전 레벨로 재귀
    if not k % 2:
        temp2 = k // 2
        if r >= temp2 and g >= temp2:
            cnt += fa(k) // (fa(temp2) ** 2) * dfs(k - 1, r - temp2, g - temp2, b)
        if g >= temp2 and b >= temp2:
            cnt += fa(k) // (fa(temp2) ** 2) * dfs(k - 1, r, g - temp2, b - temp2)
        if r >= temp2 and b >= temp2:
            cnt += fa(k) // (fa(temp2) ** 2) * dfs(k - 1, r - temp2, g, b - temp2)

    # 레벨을 세가지 색으로 채우고 이전 레벨로 재귀
    if not k % 3:
        temp3 = k // 3
        if r >= temp3 and g >= temp3 and b >= temp3:
            cnt += fa(k) // (fa(temp3) ** 3) * dfs(k - 1, r - temp3, g - temp3, b - temp3)

    # 가능한 모든 경우의 수 기록을 완료하고 리턴
    return cnt


n, r, g, b = map(int, input().split())
print(dfs(n, r, g, b))