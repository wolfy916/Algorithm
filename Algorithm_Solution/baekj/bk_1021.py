'''
회전하는 큐 - 백준(실버3)
분류 : 연결리스트
'''
import sys

class Link:
    def __init__(self, n):
        self.p = 1
        self.dct = {i: [i-1, i+1] for i in range(1, n+1)}
        self.dct[1][0] = n
        self.dct[n][1] = 1
        self.answer = 0

    def pick(self):
        pre, nxt = self.dct[self.p]
        self.dct[pre][1] = nxt
        self.dct[nxt][0] = pre
        del self.dct[self.p]
        self.p = nxt

    def check(self, num):
        cnt1 = cnt2 = 1
        tmp1 = tmp2 = self.p
        while self.dct[tmp1][0] != num:
            cnt1 += 1
            tmp1 = self.dct[tmp1][0]
        while self.dct[tmp2][1] != num:
            cnt2 += 1
            tmp2 = self.dct[tmp2][1]
        return min(cnt1, cnt2)

    def move(self, num):
        if self.p != num:
            self.answer += self.check(num)
            self.p = num
def input():
    return sys.stdin.readline().rstrip('\n')

if __name__ == '__main__':
    N, M = map(int, input().split())
    orders = tuple(map(int, input().split()))

    link = Link(N)
    for order in orders:
        link.move(order)
        link.pick()

    print(link.answer)