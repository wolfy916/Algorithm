# Queen을 두는 함수 설정
# 진수의 굿코드
def queen(n):
    global ans
    # 종료 조건. N개의 Queen을 둘 수 있으면 ans +1 적립
    if n == N + 1:
        ans += 1
        return

    # 2차원 체스판을 1차원 리스트로 축약하여 푼다.
    # 1차원 리스트의 각 원소는 체스판에서의 n번 열을 의미한다.
    # 1열(n=1)부터 순서대로 n행에 퀸을 둔다.
    for i in range(1, N + 1):
        flag = 0
        board[n] = i

        # 유효성 검증
        # 앞서 둔 퀸들과 범위가 겹친다면 continue, 그렇지 않다면 재귀한다.
        for j in range(1, n):
            if board[n] == board[j] or abs(board[n] - board[j]) == abs(n - j):
                board[n] = 0
                flag = 1
                break
        if flag == 0:
            queen(n + 1)
            board[n] = 0
        elif flag == 1:
            continue


# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [0] * (N + 1)
    ans = 0
    queen(1)
    print(f'#{test_case} {ans}')