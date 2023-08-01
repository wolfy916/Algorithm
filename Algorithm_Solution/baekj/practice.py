def get_dist(i, j, k, l):
    if i == k and j == l:
        distance = -1
    elif i == k:
        distance = abs(j-l) - 1
    elif j == l:
        distance = abs(i-k) - 1
    elif abs(i-k)>=1 and abs(j-l) >=1:
        distance = max(abs(i-k)-1,abs(j-l)-1)
    return distance

n, m = map(int, input().split())

array = []
total_dist_list = []
second_min_values = []

for _ in range(n):
    row = list(map(int, (input().split())))
    array.append(row)

for i in range(n):
    for j in range(m):
        globals()[f'dist_list_{i}{j}'] = []
        if array[i][j] == 1:
            for k in range(n):
                for l in range(m):
                    distance = get_dist(i,j,k,l)
                    globals()[f'dist_list_{i}{j}'].append(distance)
        if globals()[f'dist_list_{i}{j}'] != []:
            total_dist_list.append(globals()[f'dist_list_{i}{j}'])

print(total_dist_list)
# print(zip(*total_dist_list))

for i in zip(*total_dist_list):
    print(i)
    sorted_values = sorted(val for val in i if val != -1)
    if len(sorted_values) > 1:
        second_min_values.append(sorted_values[0])
    else:
        second_min_values.append(0)

print(max(second_min_values))