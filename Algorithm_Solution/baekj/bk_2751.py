import sys

N = int(input())
num_list = []
for i in range(N):
    num_list += [int(sys.stdin.readline())]
    if i == 0:
        continue
    else:
        for j in range(i, -1, -1):
            for k in range(j-1, -1, -1):
                if num_list[k] > num_list[j]:
                    num_list[k], num_list[j] = num_list[j], num_list[k]
for l in num_list:
    print(l)
