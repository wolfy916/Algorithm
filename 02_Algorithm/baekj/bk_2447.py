def star(n):
    if n == 1:
        return ['*']

    staryy_night = star(n // 3)
    area = []

    for i in staryy_night:
        area += [i * 3]
    for j in staryy_night:
        area += [j + ' ' * (n // 3) + j]
    for k in staryy_night:
        area += [k * 3]

    return area


print('\n'.join(star(int(input()))))