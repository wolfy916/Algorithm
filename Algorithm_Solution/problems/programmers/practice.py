a = 100
b = 100
c = [10]

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    i = -1
    while i < len(truck_weights) - 1:
        while i < len(truck_weights) - 1 and cur_weight + truck_weights[i+1] <= weight:
            answer += 1
            i += 1
            cur_weight += truck_weights[i]
        cur_weight = 0
        answer += bridge_length
    return answer

print(solution(a, b, c))