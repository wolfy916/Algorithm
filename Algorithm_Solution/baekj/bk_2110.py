# 공유기 설치

N, C = map(int, input().split())
houses = [int(input()) for house in range(N)]

houses.sort()  # 집들을 오름차순으로 정렬

start = 1
end = houses[-1] - houses[0]
d_ls = [houses[0]]  # d_ls : device_locations ; 공유기를 설치할 집 리스트
result = 0
while start < end:

    s_d = (start + end) // 2  # s_d : standard_device ; 기준이 되는 거리
    d_cnt = 1                 # d_cnt : device_count ; 해당 s_d로 몇 번 설치가 가능한지 기록
    for house in houses:             #
        if s_d <= house - d_ls[-1]:  # 마지막으로 설치된 공유기와 집간의 거리가 기준 거리 이상이면 공유기 설치
            d_ls += [house]          # 공유기 설치 리스트에 append
            d_cnt += 1               # 공유기 설치 개수 += 1

    if d_cnt >= C:
        result = s_d
        start = s_d + 1
    elif d_cnt < C:
        end = s_d

    d_ls = [houses[0]]  # d_ls 초기화

if C == 2:
    result = houses[-1] - houses[0]

print(result)