# 반도체 설계
# 좌측 포트가 오름차순일때 연결되는 우측 포트들이 모두 오름차순이면 꼬임 없이 연결됨
# 좌측 포트들이 오름차순으로 정렬되어있는셈이기 때문에 가능했던 풀이
# 정렬이 안되어있었거나 입력 크기가 조금이라도 더 컸다면 통과안되는 기본 LIS 코드
n = int(input())
ports = [0] + list(map(int, input().split()))
dp = [1]*(n+1)
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if ports[i] < ports[j]:
            # dp[j] = j번 포트까지의 최장 부분 증가 수열의 길이
            dp[j] = max(dp[i]+1, dp[j])
print(max(dp))