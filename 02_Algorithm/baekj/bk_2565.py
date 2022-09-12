# 전깃줄

def select(idx_list):  # 교차점의 갯수가 같은 전깃줄들끼리 교차점이 있는지 확인
    arr = [0] * len(idx_list)
    for i in range(len(idx_list)):
        for idx in idx_list:
            if idx in cross_point[idx_list[i]]:
                arr[i] += 1
    return idx_list[arr.index(min(arr))]  # 가장 교차점이 적은 전깃줄 인덱스를 반환


n = int(input())
lines = []
cross_point = [[] for _ in '_' * n]  # 각 전깃줄과 만나는 전깃줄들의 인덱스를 2차원 리스트로 저장
for i in range(n):
    lines += [list(map(int, input().split()))]
    a, b = lines[-1][0], lines[-1][1]
    for j in range(len(lines)):
        if a == lines[j][0]:
            continue
        elif a > lines[j][0] and b < lines[j][1]:
            cross_point[i] += [j]
            cross_point[j] += [i]
        elif a < lines[j][0] and b > lines[j][1]:
            cross_point[i] += [j]
            cross_point[j] += [i]

len_list = [0] * n
for k in range(n):  # len_list : 각 전깃줄들의 교차점 갯수
    len_list[k] = len(cross_point[k])

cnt = 0
while len_list.count(0) != n:  # 교차점 갯수가 모두 0이면 종료
    max_len = max(len_list)  # 각 전깃줄의 교차점 갯수 리스트에서 max값
    if len_list.count(max_len) == 1:  # 교차점 갯수가 같은 전깃줄이 1개라면
        max_Idx = len_list.index(max_len)
    else:  # 교차점 갯수가 같은 전깃줄이 2개 이상이라면
        index_list = []  # 조건에 해당하는 전깃줄들의 인덱스를 담을 리스트
        for l in range(n):
            if max_len == len_list[l]:
                index_list += [l]
        max_Idx = select(index_list)  # select 함수 호출

    for line_Idx in cross_point[max_Idx]:  # max_Idx의 전깃줄과 만나는 모든 전깃줄들의 인덱스
        len_list[line_Idx] -= 1  # 교차점 갯수 -1
        cross_point[line_Idx].remove(max_Idx)  # 만나는 전깃줄들 중 max_Idx의 전깃줄 인덱스를 지움

    cross_point[max_Idx].clear()
    len_list[max_Idx] = 0
    cnt += 1

print(cnt)