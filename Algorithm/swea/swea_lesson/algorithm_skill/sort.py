# 버블 정렬
# O(n**2)
# 가장 느린 정렬 알고리즘
def bubblesort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# 병합 정렬
# 컴퓨터과학 역사상 최고의 천재 -> 존 폰 노이만이 1945년에 고안
# 분할 정복의 진수
# 최선 = 최악 = O(nlogn)으로 일정한 알고리즘
# 대부분의 퀵 정렬보다 느림
# 일정한 실행 속도뿐만 아니라 안정 정렬(Stable sort)
# Stable sort : 기존의 정렬 순서가 유지됨
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

def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr

    mid = length // 2
    left = merge_sort(arr[:mid])  # left
    right = merge_sort(arr[mid:])  # right

    return merge(left, right)


# 퀵 정렬
# 영국의 컴퓨터과학자 토니 호어가 1959년에 고안
# 피벗을 기준으로 좌우를 나누는 특징 때문에 파티션 교환 정렬(Partition-Exchange sort)라고도 불림
# 최악 : O(n**2)
# Unstable sort : 기존의 정렬 순서가 무시됨
# 여러 가지 변형과 개선 버전이 있지만 N.Lomuto가 구현한 파티션 계획(Partition Scheme)를 살펴본다.
def quick_sort(arr, lo, hi):
    # 로무토 파티션 -> 항상 맨 오른쪽의 피벗을 택함
    # 토니 호어가 고안한 최초의 퀵 정렬 보다 간결하고 이해하기 쉬움
    def partition(lo, hi):
        pivot = arr[hi]
        left = lo
        for right in range(lo, hi):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        arr[left], arr[hi] = arr[hi], arr[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick_sort(arr, lo, pivot-1)
        quick_sort(arr, pivot+1, hi)


# 반복을 이용한 선택정렬
def SelectionSort(arr):
    lenV = len(arr)
    for i in range(0, lenV-1):
        minI = i
        for j in range(i+1, lenV):
            if arr[j] < arr[minI]:
                minI = j
        arr[minI], arr[i] = arr[i], arr[minI]