# K번째 수
# 모범답안 참고 코드

N = int(input())  # 1 <= N <= 100,000
K = int(input())  # 1 <= K <= min(10**9, N**2)

# 이분탐색 경계값
# B[K](K번째 수) < K인 것이 자명하므로 end = K
start, end = 1, K

while start <= end:
    # 중앙값 설정
    mid = (start + end) // 2

    # mid값이 몇번째 수인지 탐색
    # mid값보다 작거나 같은 값의 갯수를 temp에 저장
    temp = 0
    for i in range(1, N+1):
        # i = 1일때
        # 1의 배수 중 mid보다 작거나 같은 값의 갯수를 더해간다.
        # 만약, N = 5, mid = 6일 때
        # mid//i = 6개가 나온다.
        # 하지만 N = 5일때는 첫번째 줄(1의 배수)에는 5까지 밖에 없으므로
        # 6개 대신 5개를 더하도록 min 함수로 N을 설정해둔다.
        temp += min(mid//i, N)

    # mid값은 temp번째 수이다.
    if temp >= K:      # temp가 K보다 크거나 같다면
        answer = mid   # 값을 할당해두고
        end = mid - 1  # 좌측 탐색
    else:
        start = mid + 1  # temp가 K보다 작다면 우측 탐색

print(answer)