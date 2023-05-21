T = int(input())
for _ in range(1, T+1):
    tc, N = map(str, input().split())
    N = int(N)
    str_list = list(map(str, input().split()))

    str_dict = {
        'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN':9
    }

    if _ ==
    print(f'{tc}')

    for i in range(10):
        for j in range(N):
            if str_dict[str_list[j]] == i:
                print(str_list[j], end=' ')
