# swea 2063. 중간값 찾기

N = int(input())
N_list = list(map(int,input().split()))
N_list.sort()
mid_value = N_list[int((N-1)/2)]
print(mid_value)
