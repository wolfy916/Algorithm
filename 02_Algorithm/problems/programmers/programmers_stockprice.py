
prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    lenV = len(prices)
    for i in range(lenV - 1):
        for j in range(i+1, lenV):
            if prices[i] <= prices[j]:
                continue
            else:
                answer.append(j - i)
                break
        else:
            answer.append(j - i)
    return answer + [0]

print(solution(prices))