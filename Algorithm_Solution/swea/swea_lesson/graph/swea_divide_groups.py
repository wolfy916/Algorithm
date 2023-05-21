# 10014. 5248. 그룹 나누기 (제출용)

# 반복 구조

T = int(input())                           # input
for tc in range(1, T+1):                   #
    N, M = map(int, input().split())       #
    arr = list(map(int, input().split()))  #

    p = list(range(N+1))  # 대표 원소 리스트
    for i in range(M):
        a, b = arr[2*i], arr[2*i+1]

        c = 0
        if p.count(p[a]) >= p.count(p[b]):  # 대표 원소 정하기
            c = 1

        aa, bb = p[a], p[b]
        for j in range(N+1):  # 각 노드 번호들 꺼내기
            if c:
                if p[j] == bb:
                    p[j] = p[a]
            else:
                if p[j] == aa:
                    p[j] = p[b]
    print(f'#{tc} {len(set(p))-1}')

# 진수 코드 find, union 함수 사용
# # find 함수 설정
# def find(a):
#     while p[a] != a:
#          a = p[a]
#     return p[a]
#
#
# # union 함수 설정
# def union(a, b):
#     a, b = find(a), find(b)
#     if a < b:
#         p[b] = p[a]
#     else:
#         p[a] = p[b]
#
#
# # 입력값 설정
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     p = list(range(N+1))
#     for i in range(M):
#         a, b = arr[2 * i], arr[2 * i + 1]
#         union(a, b)
#
#     result = set()
#     for i in range(1, N + 1):
#         result.add(find(i))
#
#     print(f'#{tc} {len(result)}')