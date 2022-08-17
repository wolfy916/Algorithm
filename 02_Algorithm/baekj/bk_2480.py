line = list(map(int, input().split()))

if line[0] == line[1] == line[2]:
    print(10000 + line[0] * 1000)
elif line[0] == line[1]:
    print(1000 + line[0] * 100)
elif line[1] == line[2]:
    print(1000 + line[1] * 100)
elif line[0] == line[2]:
    print(1000 + line[0] * 100)
else:
    print(max(line) * 100)