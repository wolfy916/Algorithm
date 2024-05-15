'''
2024 카카오 테크 인턴십 1번문제
분류 : 인접 행렬
'''

def solution(friends, gifts):
    N = len(friends)
    idxDict = {friends[i]: i for i in range(N)}
    adjM = [[0] * N for _ in range(N)]

    for gift in gifts:
        A, B = gift.split()
        a, b = idxDict[A], idxDict[B]
        adjM[a][b] += 1

    point = [0] * N
    for a in range(N):
        send = sum(adjM[a])
        receive = sum(map(lambda x: x[a], adjM))
        point[a] = send - receive

    nxt = [0] * N
    for a in range(N - 1):
        for b in range(a + 1, N):
            if adjM[a][b] > adjM[b][a]:
                nxt[a] += 1
            elif adjM[a][b] < adjM[b][a]:
                nxt[b] += 1
            else:
                if point[a] > point[b]:
                    nxt[a] += 1
                elif point[a] < point[b]:
                    nxt[b] += 1

    return max(nxt)

friendss = [
    ["muzi", "ryan", "frodo", "neo"],
    ["joy", "brad", "alessandro", "conan", "david"],
    ["a", "b", "c"],
]
giftss = [
    ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"],
    ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"],
    ["a b", "b a", "c a", "a c", "a c", "c a"],
]
correct = [2, 4, 0]

if __name__ == '__main__':
    for i in range(3):
        print('------case', i+1)
        answer = solution(friendss[i], giftss[i])
        print('나의 답: ', answer)
        print('정답: ', correct[i])