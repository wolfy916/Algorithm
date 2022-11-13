# 멀티탭
# k: 소비전력 -> 1 <= k <= 1,000,000

# 1 <= limits의 길이 <= 10,000
# 1 <= limits[i] <= 10,000,000

# sockets의 길이 = n
# socckets[i]의 길이 = 5
# sockets[i][j] = i+1번 멀티탭의 j+1번 소켓의 연결상태를 의미
# -1 <= sockets[i][j] <= n
def solution(k, limits, sockets):

    def check(k):
        volume_lst = [0] * len(sockets)
        for i in range(5, -1, -1):
            for j in range(len(sockets)):
                if sockets[j].count(-1) + sockets[j].count(0) == i:
                    volume_lst[j] += sockets[j].count(-1) * k
                if i != 5:
                    for value in sockets[j]:
                        if value > 0:
                            volume_lst[j] += volume_lst[value-1]
        for i in range(len(volume_lst)):
            if limits[i] < volume_lst[i]:
                return False
        return True

    coordinate = []
    for i in range(len(sockets)):
        for j in range(5):
            if sockets[i][j] == -1:
                coordinate.append((i, j))

    from itertools import combinations

    if not check(k):
        for i in range(1, len(sockets)*5):
            combs = list(combinations(coordinate, i))
            for comb in combs:
                for ii, jj in comb:
                    sockets[ii][jj] = 0
                if check(k):
                    return len(comb)
                for ii, jj in comb:
                    sockets[ii][jj] = -1


k1 = 300
limits1 = [2000, 1000, 3000, 200, 600, 500]
sockets1 = [[2,3,-1,-1,-1], [4,0,-1,-1,6], [5,0,0,0,0], [-1,0,0,0,0], [-1,-1,-1,-1,-1], [-1,-1,0,0,0]]

print(solution(k1, limits1, sockets1))
