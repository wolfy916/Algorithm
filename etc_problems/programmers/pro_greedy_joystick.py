# name = "JEROEN"
name = "AAAAADBAAELSPUAAAOA"

def solution(name):
    answer = 0
    lenV = len(name)
    numberOfChangeChar = 0

    for i in range(lenV):
        if name[i] != "A":
            numberOfChangeChar += 1
            answer += min(abs(ord("A") - ord(name[i])), abs(ord("Z") - ord(name[i])) + 1)

    used = []
    if name[0] != "A":
        used = [0]

    q = [(0, used, 0)]
    while q:
        move, used, v = q.pop(0)
        if len(used) == numberOfChangeChar:
            answer += move
            break
        else:
            delta = [v - 1, v + 1]
            if v == lenV - 1:
                delta[1] = 0
            elif v == 0:
                delta[0] = lenV - 1
            for w in delta:
                if name[w] == "A":
                    q.append((move + 1, used, w))
                else:
                    if w not in used:
                        q.append((move + 1, used + [w], w))
                    else:
                        q.append((move + 1, used, w))
    return answer

print(solution(name))