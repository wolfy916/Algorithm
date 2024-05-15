# 부분집합 재귀
def powerset(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = 0
        powerset(i+1, k)
        bit[i] = 1
        powerset(i+1, k)


arr = [3, 6, 7]
n = len(arr)
bit = [0] * n
powerset(0, n)