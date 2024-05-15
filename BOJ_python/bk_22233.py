# 가희와 키워드
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 남은 키워드 개수를 반환하는 함수
def count(N, keywords, articles):
    answer = []
    cnt = N
    for article in articles:
        for key in article:
            if not keywords.get(key): continue
            if not keywords[key]: continue
            keywords[key] = False
            cnt -= 1
        answer.append(str(cnt))
    return answer

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    keywords = {input(): True for _ in range(N)}
    articles = [tuple(input().split(',')) for _ in range(M)]
    print('\n'.join(count(N, keywords, articles)))