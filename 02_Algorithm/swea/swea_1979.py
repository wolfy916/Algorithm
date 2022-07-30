# swea 1979. 어디에 단어가 들어갈 수 있을까?

# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

# [제약 사항]

# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)

# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

# [입력]

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

# 다음 줄부터 각 테스트 케이스가 주어진다.

# 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.

# 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.

# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

def PuzzleSolution():
    T = int(input())

    for i in T:
        N, K = map(int,input().split())
        pattern_area = []
        Num = 0
        
        # 퍼즐 모양 2차원 정보 입력
        for j in range(N):
            pattern_area.attend(map(int, input().split()))
        
        # 가로 테스트
        for k in range(N):
            test_word = ''
            for l in range(N):
                test_word += str(pattern_area[k][l])
            if ("1" * K) in test_word:
                Num += 1

        # 세로 테스트를 위해 

        print(f'#{i+1} {Num}')