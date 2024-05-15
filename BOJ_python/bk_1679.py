from collections import deque as dq

def check(n):
    q = dq([(0, 0)])
    visited = [False] * 50001
    while q:
        value, count = q.popleft()
        if value == n:
            return True
        if count < K:
            for num in nums:
                if visited[value + num]: continue
                if value + num <= n:
                    visited[value + num] = True
                    q.append((value + num, count + 1))
    return False

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())

    name = ["jjaksoon", "holsoon"]
    num = 1
    while check(num):
        num += 1

    print(f"{name[(num - 1) % 2]} win at {num}")