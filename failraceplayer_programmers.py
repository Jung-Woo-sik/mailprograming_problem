def solution(s,c):

    s.sort()
    c.sort()

    for par, com in zip(s, c) :
        if par != com :
            return par   # 예시 1번

    return s[-1]         # 예시 2번
