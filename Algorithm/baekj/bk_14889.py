N = int(input())
table = []

for i in range(N):
    table.append(list(map(int,input().split())))

sum_list = []
start = []
link = []
differ = []

def sum_cal(num_1,num_2):
    return table[num_1][num_2] + table[num_2][num_1]

def sum_cal_list(num):
    for i in range(num):
        for j in range(num):
            if i >= j:
                continue
            sum_list.append(sum_cal(i,j))
    backtracking()
    return differ[0]

def backtracking():
    gg