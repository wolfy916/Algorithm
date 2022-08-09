# N번째 큰 수

N = int(input())

line= list(map(int,input().split()))

for i in range(N-1):
    line += list(map(int,input().split()))
    line.sort(reverse=True)
    line = line[:N]

print(line[-1])