'''
안테나 - 백준 실버3
분류 : 정렬, 누적합, 연결리스트
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    # [1] 데이터 입력
    N = int(input())
    houses = list(map(int, input().split()))

    # [2] dict 생성
    link = dict()
    for i in range(N):
        if link.get(houses[i]):
            link[houses[i]][0] += 1
            link[houses[i]][2] += 1
        else:
            link[houses[i]] = [1, 0, 1, 0]

    # [3] 거리 계산
    houses = sorted(list(set(houses)))
    for i in range(1, len(houses)):
        diff1 = houses[i] - houses[i - 1]
        link[houses[i]][1] += diff1 * link[houses[i - 1]][0] + link[houses[i - 1]][1]
        link[houses[i]][0] += link[houses[i - 1]][0]

        j = len(houses) - i
        diff2 = houses[j] - houses[j - 1]
        link[houses[j - 1]][3] += diff2 * link[houses[j]][2] + link[houses[j]][3]
        link[houses[j - 1]][2] += link[houses[j]][2]

    # [4] 최솟값 계산
    houses.sort(key=lambda x: link[x][1] + link[x][3])
    print(houses[0])