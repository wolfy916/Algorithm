# 거짓말

N, M = map(int, input().split())
true_people = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in '_'*M]

people = [0]*(N+1)    # people[사람번호] = 1 이면 진실을 알고 있는 사람
party_check = [0]*M   # party_check[i] = 1 이면 i번째 파티는 진실 파티

if true_people.pop(0):  # 진실을 알고 있는 사람들 수
    for num in true_people:
        people[num] = 1  # 진실 체크

    q = true_people[:]   # 초기에 진실을 아는 사람들 리스트가 그대로 Queue에 들어감
    while q:
        v = q.pop(0)
        for i in range(M):  # 파티수
            if v in party[i][1:]:
                party_check[i] = 1  # 해당 인덱스 파티 체크
                for person_num in party[i][1:]:
                    if not people[person_num]:
                        people[person_num] = 1
                        q.append(person_num)

print(M - party_check.count(1))
