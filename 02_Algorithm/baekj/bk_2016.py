# 미팅 주선하기
from itertools import permutations as pr

T = int(input())
for tc in range(1, T + 1):
    man = [[1, 6, 7, 8, 9, 10]] + [[n] + list(map(int, input().split())) for n in range(2, 6)]
    woman = [[n] + list(map(int, input().split())) for n in range(6, 11)]
    couple = [0] * 6
    woman_lst = [w[:] for w in woman]
    while sum(couple) != 40:
        for w in woman_lst:
            w_num = w[0]
            for m_num in w[1:]:
                if m_num == -1:
                    continue
                if not couple[m_num]:
                    couple[m_num] = w_num
                    break
                else:
                    for m in man:
                        if m[0] == m_num:
                            cur = m.index(couple[m_num])
                            new = m.index(w_num)
                            break
                    if cur > new:
                        for i in range(len(woman_lst)):
                            if woman_lst[i][0] == couple[m_num]:
                                woman_lst[i][woman_lst[i].index(couple[m_num])] = -1
                        couple[m_num] = w_num
                        break
        woman_lst = []
        for w in woman:
            if w[0] not in couple:
                woman_lst.append(w[:])

    his_girfriend = couple[1]  # 원래 케이스에서의 최종 여자친구 번호

    if his_girfriend == 6:
        print('NO')
    else:
        perms = list(pr(range(6, 11), 5))
        for perm in perms:
            new_man = [[1] + list(perm)] + [m[:] for m in man[1:]]
            couple = [0] * 6
            woman_lst = [w[:] for w in woman]
            while sum(couple) != 40:
                for w in woman_lst:
                    w_num = w[0]
                    for m_num in w[1:]:
                        if m_num == -1:
                            continue
                        if not couple[m_num]:
                            couple[m_num] = w_num
                            break
                        else:
                            for m in new_man:
                                if m[0] == m_num:
                                    cur = m.index(couple[m_num])
                                    new = m.index(w_num)
                                    break
                            if cur > new:
                                for ww in woman_lst:
                                    if ww[0] == couple[m_num]:
                                        ww[ww.index(m_num)] = -1
                                couple[m_num] = w_num
                                break
                woman_lst = []
                for w in woman:
                    if w[0] not in couple:
                        woman_lst.append(w[:])

            if his_girfriend > couple[1]:
                print('YES')
                break
        else:
            print('NO')