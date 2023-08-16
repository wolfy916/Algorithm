from collections import deque as dq


def solution(users, emoticons):
    def check_user_reaction(discount_lst):
        temp = [0, 0]
        for per1, price1 in users:
            charge = 0
            for per2, price2 in discount_lst:
                if per1 <= per2:
                    charge += price2
                if charge >= price1:
                    temp[0] += 1
                    break
            else:
                temp[1] += charge

        if answer[0] < temp[0]:
            answer[0] = temp[0]
            answer[1] = temp[1]
        elif answer[0] == temp[0]:
            if answer[1] <= temp[1]:
                answer[1] = temp[1]

    def make_discount_set(i, lst, M):
        if len(lst) == M:
            check_user_reaction(lst)
            return
        for per in discount:
            lst.append((per, emoticons[i] * (100 - per) // 100))
            make_discount_set(i + 1, lst, M)
            lst.pop()

    answer = [0, 0]
    discount = [10, 20, 30, 40]
    make_discount_set(0, [], len(emoticons))

    return answer

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users, emoticons))