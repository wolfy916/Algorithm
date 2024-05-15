# 국회의원 선거

N = int(input())
line = [int(input()) for _ in range(N)]
cnt = 0
while True:

    if N == 1:  # 종료 조건 1
        break   # N이 1일때 cnt = 0

    maxV = max(line[1:])  # 종료 조건 2
    if line[0] > maxV:    # 후보 1을 제외한 다른 후보들의 max값보다 크면 종료
        break             #

    maxV_Idx = line[1:].index(maxV)  # 다른 후보들의 max값의 인덱스 할당
    line[maxV_Idx+1] -= 1            # max값 1 빼기
    line[0] += 1                     # 후보 1에게 1 더하기
    cnt += 1                         # 카운트

print(cnt)