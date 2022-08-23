def match(line):
    if len(line) == 2:
        a = line[0][1]
        b = line[1][1]
        if a == b:
            return line[0]
        elif a == 1 and b == 3:
            return line[0]
        elif a == 3 and b == 1:
            return line[1]
        else:
            if a > b:
                return line[0]
            else:
                return line[1]
    elif len(line) == 1:
        return line[0]

    line_len = len(line) - 1
    if len(line) > 2:
        match_line = [match(line[:(line_len//2)+1])] + [match(line[(line_len//2)+1:])]

    return match(match_line)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    i = 1
    cards_index = []
    for x in cards:
        cards_index.append((i, x))
        i += 1

    print(f'#{tc} {match(cards_index)[0]}')