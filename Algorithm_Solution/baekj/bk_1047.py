# 울타리

def check(lst):
    possible_length = 0
    maxW = maxH = 0
    minW = minH = 10000000
    for i in range(N):
        if i in lst:
            possible_length += woods[i][2]
        else:
            x, y, v = woods[i]
            if maxW < x:
                maxW = x
            if minW > x:
                minW = x
            if maxH < y:
                maxH = y
            if minH > y:
                minH = y

    length = 2 * ((maxW-minW) + (maxH-minH))

    if possible_length >= length:
        # print(f'length: {length}, survive_woods: {survive_woods}')
        # print(f'possible_length: {possible_length}, lst: {lst}')
        # print('-----------------------------------------------------------------------------------')
        return True
    else:
        return False


def powerset(i, k):
    global minV
    if i == k:
        lst = []
        for j in range(k):
            if bit[j]:
                lst.append(arr[j])
        if minV > len(lst):
            if check(lst):
                minV = len(lst)
        elif minV < len(lst):
            return
    else:
        bit[i] = 0
        powerset(i + 1, k)
        bit[i] = 1
        powerset(i + 1, k)


N = int(input())
woods = [list(map(int, input().split())) for _ in '_'*N]
minV = N

arr = range(N)
bit = [0] * N
powerset(0, N)
print(minV)