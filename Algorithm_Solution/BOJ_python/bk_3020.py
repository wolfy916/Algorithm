# 개똥벌레

N, H = map(int, input().split())  # 2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000

bottom = [0] * (H+1)  # ex) bottom[1] = 크기가 1인 석순의 갯수
top = [0] * (H+1)  # ex) top[2] = 크기가 2인 종유석의 갯수
for i in range(1, N+1):
    obstacle = int(input())
    # 홀수 -> 석순
    if i % 2:
        bottom[obstacle] += 1
    # 짝수 -> 종유석
    else:
        top[obstacle] += 1

'''
개똥벌레가 높이가 h인 경로로 날아갈 때
크기가 h 이상인 모든 석순을 부수고 지나가야함
바로 아래 누적합 for 문을 마쳤을 때
bottom[i] = 크기가 i 이상인 모든 석순의 개수 
'''

for i in range(H-1, 0, -1):
    bottom[i] += bottom[i+1]

# 종유석도 같은 방법으로 진행
for i in range(H-1, 0, -1):
    top[i] += top[i+1]
top = [0] + top[1:][::-1]  # 종유석은 거꾸로이기 때문에 뒤집어줘야함

# paths[i] = 높이가 i인 경로로 날았을 때 부숴야할 장애물 갯수
paths = [bottom[i] + top[i] for i in range(1, H+1)]

minV = min(paths)  # 최솟값
cntV = paths.count(minV)  # 최솟값 cnt
print(minV, cntV)