# 골드바흐의 추측

def BaeGoPa(num): # 소수를 판별하는 배고파 함수
    for x in range(2, num): # 2부터 num-1 까지의 수로 나누었을때 나머지가 0나오면 소수가 아님
        if num % x == 0:
            return 0 # num은 소수가 아니기 때문에 0 반환
    return 1 # num은 소수이기 때문에 1 반환


T = int(input()) # 입력
for tc in range(1, T+1):
    N = int(input())

    partition_list = [] # 파티션을 저장할 리스트 생성
    for i in range(1, N): # 입력받은 수보다 작은 수들의 조합을 다 가져온다.
        for j in range(1, N): # (0,0)부터 (N,N)까지 다 가져옴
            if i + j == N and BaeGoPa(i) and BaeGoPa(j): # 두 숫자의 합이 N인지? i와 j가 소수인지?
                partition_list += [[i, j]] # 조건 충족시 파티션 리스트에 리스트 형태의 원소로 추가
    
    minV = 10000 # 최솟값의 조합을 찾아야 하므로 탐색 ~
    for x, y in partition_list:
        if minV > abs(x-y):
            minV = abs(x-y)
            result = [x, y]
            
    print(result) # 출력
