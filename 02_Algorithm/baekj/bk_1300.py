import sys

# K번째 수
N = int(input())  # 1 <= N <= 100,000
K = int(input())  # 1 <= K <= min(10**9, N**2)
count = 1
if K == 1:
    print(1)
    sys.exit()
else:
    for i in range(1, N):
        for j in range(0, i+1):
            row, col = j + 1, i - j + 1
            if row > col:
                break
            if not i % 2 and row == col:
                count += 1
                if count == K:
                    print(row*col)
                    sys.exit()
                break
            count += 2
            if count >= K:
                print(row*col)
                sys.exit()