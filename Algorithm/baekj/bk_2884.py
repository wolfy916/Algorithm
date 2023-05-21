# 시간과 분을 입력 받고, 45분 이전의 시각을 출력해야함
# 입력
# 23 59
# 출력
# 23 14s


h,m = map(int,input().split())
print(h,m-45) if m >= 45 and h >= 0 else print(23, m+15) if m >= 0 and h == 0 else print(h-1, m+15)
