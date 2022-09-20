def in_order(r, c1, c2):
    if r:
        in_order(c1[r])
        print(r)
        in_order(c2[r])


def solution(info, edges):
    answer = 0
    wolf = 0
    sheep = 0

    chd1 = [0]*len(info)
    chd2 = [0]*len(info)
    par = [0]*len(info)

    for a, b in edges:
        if chd1:
            chd1[a] = b
        else:
            chd2[a] = b
        par[b] = a

    return answer