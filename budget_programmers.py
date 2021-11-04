def solution(d, budget):
    answer = 0
    x = budget
    cnt = 0
    d.sort()
    for i in d:
        x = x - i
        cnt = cnt +1
        if x < 0 :
            cnt = cnt -1
            break
    return cnt