# 이전 순열
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 정렬
def new_sort():
    global arr
    for i in range(N-1, 0, -1):
        if arr[i-1] > arr[i]:
            for j in range(N-1, 0, -1):
                if arr[j] < arr[i-1]:
                    arr[j], arr[i-1] = arr[i-1], arr[j]
                    return arr[:i] + sorted(arr[i:], reverse=True)
    return [-1]

# [main]
if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    print(*new_sort())