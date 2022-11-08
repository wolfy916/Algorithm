direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Player:

    def __init__(self, hx, hy, direct, stat, gun, point):
        self.x = hx
        self.y = hy
        self.d = direct
        self.s = stat
        self.g = gun
        self.p = point

    def move(self):
        ni, nj = self.x+direction[self.d][0], self.y+direction[self.d][1]
        if area[ni][nj] == '-':
            ni, nj = self.x-direction[self.d][0], self.y-direction[self.d][1]
        self.x, self.y = ni, nj

    def get_the_gun(self):
        if area[self.x][self.y] > self.g:
            area[self.x][self.y], self.g = self.g, area[self.x][self.y]

    def drop_the_gun(self):
        self.g = 0

    def lose_move(self):
        ni, nj = self.x + direction[self.d][0], self.y + direction[self.d][1]


# n: 격자의 크기, m: 플레이어의 수, k: 라운드의수
# 2 ≤ n ≤ 20, 1 ≤ m ≤ min(n**2, 30), 1 ≤ k ≤ 500
n, m, k = map(int, input().split())
players = [0] * m

#  n개의 줄에 걸쳐 격자에 있는 총의 정보, 1 ≤ 총의 공격력 ≤ 100,000
area = [['-']*(n+2)] + [['-'] + list(map(int, input().split())) + ['-'] for _ in '_' * n] + [['-']*(n+2)]

# m개의 줄에 걸쳐 플레이어들의 정보
# (x, y): 플레이어의 위치, d: 방향, s: 플레이어의 초기 능력치
# 방향 d는 0부터 3까지 순서대로 ↑, →, ↓, ←을 의미
# 1 ≤ s ≤ 100, 1 ≤ x, y ≤ n
for i in range(m):
    x, y, d, s = map(int, input().split())
    players[i] = Player(x, y, d, s)
