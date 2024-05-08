# 골드바흐의 추측

# [A] 소수 리스트 생성 함수
def gen_lst(v):
    lst = [False, False] + [True] * (v + 1)
    for i in range(2, v + 1):
        if not lst[i]: continue
        for j in range(i * 2, v + 1, i):
            lst[j] = False
    return lst

# [main]
if __name__ == '__main__':
    T = int(input())
    nums = [int(input()) for _ in range(T)]

    # 입력값 중 최대값으로 소수 리스트 생성
    lst = gen_lst(max(nums))

    # 골드바흐 파티션 출력
    for num in nums:
        for i in range(num // 2, -1, -1):
            if lst[i] and lst[num - i]:
                print(i, num - i)
                break