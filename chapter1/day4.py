

def solution(n, computers):
    answer = 0
    traveled = set()
    def dfs(travel):
        if travel in traveled:
            return
        traveled.add(travel)
        for i in range(n):
            if computers[travel][i] == 1:
                dfs(i)
        return
    for i in range(n):
        if not i in traveled:
            answer += 1
            dfs(i)
    return answer
