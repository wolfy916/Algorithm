h, m = map(int, input().split())
t = int(input())
print((h+t//60+(m+t%60>=60))%24,(m+t%60)%60)