# string 실습 가장 빠른 문자열 타이핑

T = int(input())
for tc in range(1, T+1):
    A, B = map(list, input().split())  # 각 알파벳을 원소로 받는 리스트로 할당

    # 각 리스트의 길이 계산
    A_len = 0
    for _ in A:
        A_len += 1
    B_len = 0
    for _ in B:
        B_len += 1

    result = 0  # result : B의 단어가 A에 있다면 result += 1
    result_Idx = 0  # index 뛰어넘기
    for i in range(A_len-B_len+1):
        if result_Idx > i:
            continue

        cnt = 0  # B의 알파벳이 A의 알파벳과 같다면 cnt += 1
        for j in range(B_len):
            if B[j] == A[i+j]:
                cnt += 1
        if cnt == B_len:  # cnt가 B의 길이와 같다면 단어가 일치
            result += 1
            result_Idx = i + B_len

    result = A_len - (result * (B_len - 1))

    print(f'#{tc} {result}')