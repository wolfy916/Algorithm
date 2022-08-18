T = int(input())
for tc in range(1, T+1):
    result = list(input())
    scores = []
    sumV = 0
    for x in result:
        if x == 'O':
            scores += [x]
            sumV += len(scores)
        else:
            scores.clear()
    print(sumV)