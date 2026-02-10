def hanoi(start, end, n):
    if n == 1:
        return [[start, end]]
    middle = 1+2+3-start-end
    return hanoi(start, middle, n-1) + [[start, end]] + hanoi(middle, end, n-1)    

def solution(n):
    answer = [[]]
    answer = hanoi(1,3,n)
    return answer
