# 암호만들기
from itertools import combinations

L, C = map(int, input().split())
chars = list(input().split())

group1 = []
group2 = []
vowels = ['a', 'e', 'i', 'o', 'u']
for char in chars:
    if char in vowels:
        group1 += [char]
    else:
        group2 += [char]

lst = list(map(list, combinations(chars, L)))
lst = list(map(sorted, lst))
for i in range(L-1, -1, -1):
    lst.sort(key=lambda x: x[i])

for arr in lst:
    cnt1 = cnt2 = 0
    for char1 in group1:
        if char1 in arr:
            cnt1 += 1
    for char2 in group2:
        if char2 in arr:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        print(''.join(arr))
