import sys

restV_list = []
for i in range(10):
    restV_list += [(int(sys.stdin.readline())) % 42]

print(len(set(restV_list)))