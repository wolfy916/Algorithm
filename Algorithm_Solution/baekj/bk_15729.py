N = int(input())    # 버튼의 개수

num = list(map(int, input().split()))    # 쪽지에 적혀있는 N자리의 수

current = [0] * N  # 현재 불이 다 꺼져있는 상태의 배열(0이니까 False)

cnt = 0     # 바꾸는 횟수를 누적해서 더할 변수
for i in range(N):
    if num[i] != current[i]:    # 두 값이 다르면
        cnt += 1
        current[i] = 1 - current[i] # 바꿔주기(boolean 개념)
        print(current)

        # 오른쪽으로 두칸까지 영향을 미치므로 체크해주기
        # 체크 안하면 리스트 인덱스가 범위를 벗어나게 됨.
        if i+1 < N:
            current[i+1] = 1 - current[i+1]
        if i+2 < N:
            current[i+2] = 1 - current[i+2]

print(cnt)