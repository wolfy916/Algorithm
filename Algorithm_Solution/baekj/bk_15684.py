# 사다리 조작

def comb(n, r, s, t):
    global result, end

    if end:  # 재귀 도중 냅다 종료
        return

    if r == 0:  # 조합 1개 완성
        test = []  # 백트래킹을 위한 리스트, 경로 틀리면 사다리 다시 철거해야함 ㅠ

        if len(comb_arr) == 2:  # 조합 완성 시, 같은 행내에서 열의 차이값이 1이 나오면 버려야함
            ni1, nj1 = (comb_arr[0]//(N-1))+1, (comb_arr[0] % (N-1)) + 1            # 1차원 위치 번호를 다시 2차원 인덱스화
            ni2, nj2 = (comb_arr[1] // (N - 1)) + 1, (comb_arr[1] % (N - 1)) + 1    #
            if ni1 == ni2 and abs(nj1-nj2) == 1:
                return

        elif len(comb_arr) == 3:  # 조합 완성 시, 같은 행내에서 열의 차이값이 1이 나오면 버려야함
            ni1, nj1 = (comb_arr[0] // (N - 1)) + 1, (comb_arr[0] % (N - 1)) + 1  # 1차원 위치 번호를 다시 2차원 인덱스화
            ni2, nj2 = (comb_arr[1] // (N - 1)) + 1, (comb_arr[1] % (N - 1)) + 1  #
            ni3, nj3 = (comb_arr[2] // (N - 1)) + 1, (comb_arr[2] % (N - 1)) + 1  #
            if ni1 == ni2 and abs(nj1 - nj2) == 1:
                return
            elif ni1 == ni3 and abs(nj1 - nj3) == 1:
                return
            elif ni2 == ni3 and abs(nj2 - nj3) == 1:
                return

        # 사다리 설치 !
        for num in comb_arr:
            n_i = (num // (N-1)) + 1
            n_j = (num % (N-1)) + 1
            area[n_i][n_j] = 1
            area[n_i][n_j+1] = -1
            test.append((n_i, n_j))

        if path_check():  # 사다리 설치 후, 경로 검사
            result = t    # 정답 찾음
            end = 1       # 재귀 얼른 종료시키기
            return
        else:
            for n_i, n_j in test:  # 올바른 경로가 아니었다면 방금 설치한 사다리 철거
                area[n_i][n_j] = 0
                area[n_i][n_j + 1] = 0
    else:
        for i in range(s, n-r+1):  # combination
            comb_arr[r-1] = ladder[i]
            comb(n, r-1, i+1, t)
            if end:  # 답 찾으면 재귀 종료
                return


# 모든 경로가 올바른지 확인, 하나라도 비정상적이면 False
def path_check():
    for j in range(1, N+1):
        s_i, s_j = 1, j
        while s_i != H+1:
            if area[s_i][s_j]:
                s_j += area[s_i][s_j]
            s_i += 1
        if s_j != j:
            return False
    return True


N, M, H = map(int, input().split())
area = [[0]*(N+1) for _ in '_'*(H+2)]
ladder = list(range((N-1)*H))  # 사다리를 설치할 수 있는 위치를 1차원 배열로 표현 -> 이 번호를 이용해서 조합 사용

for _ in '_'*M:
    a, b = map(int, input().split())
    area[a][b] = 1
    area[a][b+1] = -1

    # a, b를 이용하여 사다리 번호화 ex) (1, 1) -> 사다리 0번
    Idx = (a-1)*(N-1)+b-1
    if Idx in ladder:
        ladder.remove(Idx)  # 문제에서 준 사다리는 리스트에서 제거

    # N이 2가 아닐 때
    if N != 2:

        # 맨 왼쪽 사다리일 경우, 오른쪽에 사다리를 설치 할 수 없으므로 해당 사다리 번호 제거
        if b == 1 and Idx+1 in ladder:
            ladder.remove(Idx+1)
        # 맨 오른쪽 사다리일 경우, 왼쪽에 사다리를 설치 할 수 없으므로 해당 사다리 번호 제거
        elif b == N-1 and Idx-1 in ladder:
            ladder.remove(Idx-1)
        # 맨 왼쪽도, 맨 오른쪽도 아닐 경우, 양 옆에 사다리 설치 불가하므로 양 옆 사다리 번호 제거
        else:
            if Idx+1 in ladder:
                ladder.remove(Idx+1)
            if Idx-1 in ladder:
                ladder.remove(Idx-1)

result = -1  # default
end = 0      # 재귀함수의 리턴 조건
if not path_check():  # 사다리 설치전 경로 검사
    for i in range(1, 4):  # 사다리 1개 설치부터 3개 설치까지
        comb_arr = [0] * i  # 사다리 설치할 위치 번호 조합을 위한 배열
        comb(len(ladder), i, 0, i)  # 조합 시작
        if end:
            break
else:  # 사다리 설치 안해도 정상
    result = 0

print(result)