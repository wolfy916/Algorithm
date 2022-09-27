# 5205. [구현] 4일차 - 퀵 정렬
def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)


def partition(A, l, r):  # Hoare-Partition
    p = A[l]  # pivot
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quickSort(arr, 0, N-1)

    print(f'#{tc} {arr[N//2]}')
