# swea 2058. 자릿수 더하기

num = str(input())
num_list = []
for i in num:
    num_2 = int(i)
    num_list.append(num_2)
print(sum(num_list))