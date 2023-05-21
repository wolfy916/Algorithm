info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# Lower bound
# 정렬 된 배열(nums)에서 찾고자 하는 값(target) 이상이 처음 나타나는 위치
# nums[k-1] < target 이고 nums[k] >= target인 k를 찾는다

def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right

def solution(info, query):
    answer = []

    list1 = ["cpp", "java", "python"]
    list2 = ["backend", "frontend"]
    list3 = ["junior", "senior"]
    list4 = ["pizza", "chicken"]

    userPool = dict()
    for item in info:
        k1, k2, k3, k4, score = item.split(" ")
        k1 = [k1, '-']
        k2 = [k2, '-']
        k3 = [k3, '-']
        k4 = [k4, '-']
        for s1 in k1:
            for s2 in k2:
                for s3 in k3:
                    for s4 in k4:
                        userKey = s1+s2+s3+s4
                        if userKey not in userPool.keys():
                            userPool[userKey] = [int(score)]
                        else:
                            userPool[userKey].append(int(score))

    for userKey in userPool.keys():
        userPool[userKey].sort()

    for order in query:
        o1, o2, o3, o4 = order.split(" and ")
        o4, score = o4.split()
        score = int(score)
        userKey = o1+o2+o3+o4
        cnt = 0
        if userKey in userPool.keys():
            cnt = len(userPool[userKey]) - lower_bound(userPool[userKey], score)
        answer.append(cnt)
    return answer

# [1,1,1,1,2,4]
print(solution(info, query))