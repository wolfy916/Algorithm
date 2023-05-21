# 10954. 5204. 4일차 - 병합정렬(제출용)

def merge(left, right):
    result = []

    i = j = 0
    l, r = len(left), len(right)
    while i < l or j < r:
        if i < l and j < r:  # 양 쪽 다 원소가 남아있는 경우
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < l:  # 왼쪽만 원소가 남아있는 경우
            result.append(left[i])
            i += 1
        elif j < r:  # 오른쪽만 원소가 남아있는 경우
            result.append(right[j])
            j += 1

    return result


def merge_sort(lst):
    global cnt
    length = len(lst)
    if length == 1:
        return lst

    mid = length // 2
    left = merge_sort(lst[:mid])  # left
    right = merge_sort(lst[mid:])  # right
    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    sorted_arr = merge_sort(arr)

    print(f'#{tc} {sorted_arr[N//2]} {cnt}')

