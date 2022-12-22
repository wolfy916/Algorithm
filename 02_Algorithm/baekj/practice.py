# 크리스마스 트리

# [A] 팩토리얼 함수
def fa(n):
    if n == 1:
        return 1
    return n * fa(n - 1)


# [B] k레벨에서 현재 갖고 있는 r, g, b로 가능한 경우의 수를 cnt에 기록하여 리턴하는 재귀함수
def dfs(k, r, g, b):
    # 경우의 수를 기록할 변수 선언 및 초기화
    cnt = 0

    # 입력값 n보다 큰 레벨이라면 리턴 1
    if k > n:
        return 1

    # 레벨을 하나의 색으로 채우고 다음 레벨로 재귀
    if r >= k:
        # 하나의 색으로 채우는 방법은 1가지 뿐이므로 곱셈이 없다.
        cnt += dfs(k + 1, r - k, g, b)
    if g >= k:
        cnt += dfs(k + 1, r, g - k, b)
    if b >= k:
        cnt += dfs(k + 1, r, g, b - k)

    # 레벨을 두가지 색으로 채우고 다음 레벨로 재귀
    if not k % 2:  # 짝수 레벨
        temp2 = k // 2
        if r >= temp2 and g >= temp2:
            # ex) 레벨 4의 4칸을 2가지 색으로 채우는 경우의 수는
            #     4!//(2! * 2!) 이다.
            #     레벨 n의 n칸을 2가지 색으로 채우는 경우의 수는
            #     n!//((n//2)! * (n//2)!) = n!//((n//2)!**2) 이다.
            cnt += fa(k) // (fa(temp2) ** 2) * dfs(k + 1, r - temp2, g - temp2, b)
        if g >= temp2 and b >= temp2:
            cnt += fa(k) // (fa(temp2) ** 2) * dfs(k + 1, r, g - temp2, b - temp2)
        if r >= temp2 and b >= temp2:
            cnt += fa(k) // (fa(temp2) ** 2) * dfs(k + 1, r - temp2, g, b - temp2)

    # 레벨을 세가지 색으로 채우고
    # 다음 레벨로 재귀
    if not k % 3:  # 3의 배수인 레벨
        temp3 = k // 3
        if r >= temp3 and g >= temp3 and b >= temp3:
            # ex) 레벨 9의 9칸을 3가지 색으로 채우는 경우의 수는
            #     9!//(3!**3) 이다.
            cnt += fa(k) // (fa(temp3) ** 3) * dfs(k + 1, r - temp3, g - temp3, b - temp3)

    # k보다 크거나 같고, n보다 작거나 같은 레벨들의 경우의 수를 모두 기록하고 리턴
    return cnt


n, r, g, b = map(int, input().split())
print(dfs(1, r, g, b))  # 1레벨부터 탐색