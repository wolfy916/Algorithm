def solution(alp, cop, problems):
    def possible_check(cur_alp, cur_cop, possible):
        for i in range(len(problems)):
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
            if i not in possible:
                if alp_req <= cur_alp and cop_req <= cur_cop:
                    possible.append(i)
        return possible

    def dfs(cur_alp, cur_cop, cur_cost, possible):
        possible = possible_check(cur_alp, cur_cop, possible)

        if answer[0] and cur_cost >= answer[0]:
            return

        if (cur_alp, cur_cop) == (max_alp, max_cop):
            answer[0] = min(answer[0], cur_cost) if answer[0] else cur_cost
            return

        for i in possible:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
            dfs(cur_alp + alp_rwd, cur_cop + cop_rwd, cur_cost + cost, possible)

        dfs(cur_alp + 1, cur_cop, cur_cost + 1, possible)
        dfs(cur_alp, cur_cop + 1, cur_cost + 1, possible)

    answer = [0]
    max_alp = max_cop = 0

    for i in range(len(problems)):
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    dfs(alp, cop, 0, [])

    return answer[0]

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))