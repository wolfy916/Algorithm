# 소프티어 업무 처리
import sys

# [A] 메인 함수
def solution():
    # [B] 입력 함수 초기화
    def input():
        return sys.stdin.readline().rstrip('\n')

    # [C] 말단 직원 업무 진행 함수
    def staff_task():
        nonlocal staffs, tree1, tree2
        for staff in staffs.keys():
            if staffs[staff]:
                if staff % 2 == 0:
                    tree1[staff // 2].append(staffs[staff].pop(0))
                else:
                    tree2[staff // 2].append(staffs[staff].pop(0))

    # [1] 데이터 입력 및 초기화
    H, K, R = map(int, input().split())
    tree1 = [[] for _ in range(2 ** H)]
    tree2 = [[] for _ in range(2 ** H)]
    staffs = dict()
    for i in range(2 ** H, 2 ** (H + 1)):
        staffs[i] = list(map(int, input().split()))

    # [2] 날짜수 R만큼 업무 진행
    answer = day = 0
    while day < R:
        day += 1
        today_is_odd = bool(day % 2)
        # [2-1] 부서장 업무 수행
        if today_is_odd:
            if tree1[1]:
                answer += tree1[1].pop(0)
        else:
            if tree2[1]:
                answer += tree2[1].pop(0)

        # [2-2] 부서장과 말단을 제외한 모든 직원들 업무 수행
        for i in range(2, 2 ** H):
            if today_is_odd:
                if tree1[i]:
                    if i % 2 == 0:
                        tree1[i // 2].append(tree1[i].pop(0))
                    else:
                        tree2[i // 2].append(tree1[i].pop(0))
            else:
                if tree2[i]:
                    if i % 2 == 0:
                        tree1[i // 2].append(tree2[i].pop(0))
                    else:
                        tree2[i // 2].append(tree2[i].pop(0))

        # [2-3] 말단 직원 업무 수행
        staff_task()

    return answer

print(solution())