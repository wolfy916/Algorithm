chars1 = input()
chars2 = input()
l1 = len(chars1)
l2 = len(chars2)

ismax = 0
for i in range(l1):
    cnt = 0
    for j in range(l2-ismax):
        compare1 = chars1[i:i+ismax]
        compare2 = chars2[j:j+ismax]
        if compare1 == compare2:
            di, dj = i+ismax, j+ismax
            cnt += ismax
            try:
               while chars2[dj] == chars1[di]:
                   cnt += 1
                   dj += 1
                   di += 1
            except IndexError:
               pass
            if ismax < cnt:
               ismax = cnt
            cnt = 0

print(ismax)