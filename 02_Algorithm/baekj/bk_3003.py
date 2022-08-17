line = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
for i in range(6):
    line[i] = chess[i] - line[i]
print(' '.join(list(map(str, line))))