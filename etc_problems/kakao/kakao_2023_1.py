today = '2022.05.19'
terms = ['A 6', 'B 12', 'C 3']
privacies = ['2021.05.02 A', '2021.07.01 B', '2022.02.19 C', '2022.02.20 C']

today = list(map(int, today.split('.')))
dict_terms = {}
for t in terms:
    alpha, months = t.split()
    dict_terms[alpha] = int(months)
list_privacies = [list(p.split()) for p in privacies]

result = []
i = 0
for day, alpha in list_privacies:
    i += 1
    date = list(map(int, day.split('.')))
    plus_days = dict_terms[alpha] * 28
    yy, mm, dd = date[0], date[1], date[2]

    while plus_days != 0:
        plus_days -= 1

        dd += 1

        if dd == 29:
            mm += 1
            dd -= 28

        if mm == 13:
            yy += 1
            mm -= 12

    dd -= 1

    if yy == today[0]:
        if mm == today[1]:
            if dd == today[2]:
                continue
            elif dd < today[2]:
                result.append(i)
            else:
                continue
        elif mm < today[1]:
            result.append(i)
        else:
            continue
    elif yy < today[0]:
        result.append(i)
    else:
        continue

print(result)