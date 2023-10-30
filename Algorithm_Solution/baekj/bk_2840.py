'''
행운의 바퀴 - 백준(실버4)
분류 : 연결리스트
'''
import sys

class Circle:
    def __init__(self, n):
        self.p = 0
        self.arr = ['?'] * n
        self.size = n

    def cur(self):
        return self.arr[self.p]

    def move(self, num, char):
        self.p += num
        self.p %= self.size
        if self.cur() == '?':
            if char in self.arr:
                return False
            self.arr[self.p] = char
        elif self.cur() != char:
            return False
        return True

    def answer(self):
        for i in range(self.p, -1, -1):
            print(self.arr[i], end='')
        for i in range(self.size-1, self.p, -1):
            print(self.arr[i], end='')

def input():
    return sys.stdin.readline().rstrip('\n')

if __name__ == '__main__':
    N, K = map(int, input().split())
    circle = Circle(N)
    for _ in range(K):
        num, char = input().split()
        if not circle.move(int(num), char):
            print('!')
            break
    else:
        circle.answer()
