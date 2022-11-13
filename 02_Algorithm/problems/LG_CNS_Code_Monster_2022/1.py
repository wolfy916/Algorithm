# 구슬
# 1 <= 구슬의 개수 <= 9
# marbles[i]는 i+1번 구슬의 무게
# ex) marbles[0] = 1번 구슬의 무게

'''
1. 받침대 기준 좌우 구슬 차이가 적을수록
2. 더 많은 구슬 사용할수록
3. 구슬의 무게 합이 더 높을수록
4. 사전순으로 더 빠른 장식일수록
'''


def solution(marbles):

    def check(temp, check_lst):
        a_len = len(temp)
        b_len = len(check_lst)

        # 1번 기준
        if a_len % 2:
            a_differ = abs(len(temp[:a_len//2]) - len(temp[a_len//2+1:]))
        else:
            a_differ = abs(len(temp[:a_len//2]) - len(temp[a_len//2:]))

        if b_len % 2:
            b_differ = abs(len(temp[:b_len//2]) - len(temp[b_len//2+1:]))
        else:
            b_differ = abs(len(temp[:b_len//2]) - len(temp[b_len//2:]))

        if a_differ > b_differ:
            return True
        elif a_differ == b_differ:
            # 2번 기준
            if a_len < b_len:
                return True
            elif a_len == b_len:
                # 3번 기준
                if sum(temp) < sum(check_lst):
                    return True
                elif sum(temp) == sum(check_lst):
                    # 4번 기준
                    check_lst = list(check_lst)
                    if int(''.join(map(str, temp))) > int(''.join(map(str, check_lst))):
                        return True
        return False

    from itertools import combinations, permutations

    answer = 0
    n = len(marbles)
    for i in range(n - 1):
        combs = list(combinations(marbles, n - i))
        for comb in combs:
            perms = set(permutations(comb))
            for perm in perms:
                len_perm = n - i
                if len_perm % 2:
                    if sum(perm[:len_perm//2]) != sum(perm[len_perm//2+1:]):
                        continue
                else:
                    if sum(perm[:len_perm//2]) != sum(perm[len_perm//2:]):
                        continue

                if not answer:
                    answer = perm
                    continue

                if check(answer, perm):
                    answer = list(perm[:])

    return list(answer)


marbles = [1, 2, 3, 4, 4]
print(solution(marbles))