# 못 품

N = int(input())
line = list(map(int, input().split()))

if line == sorted(line):
    print(-1)
else:
    for i in range(N-1, -1, -1):
        if line[i-1] > line[i]:
            for j in range(N-1, i-1, -1):
                if line[i-1] > line[j]:
                    line[i-1], line[j] = line[j], line[i-1]
                    maxV = i-1
                    break
            break
    if maxV == -1:
        print(line)
    else:
        line = line[:maxV+1] + sorted(line[maxV+1:], reverse = True)
        print(line)




# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2

# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# 2 4 3 1

# 3 1 2 4
# 3 1 4 2
# 3 2 1 4
# 3 2 4 1
# 3 4 1 2
# 3 4 2 1

# 4 1 2 3
# 4 1 3 2
# 4 2 1 3
# 4 2 3 1
# 4 3 1 2
# 4 3 2 1