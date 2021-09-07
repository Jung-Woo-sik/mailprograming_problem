def solution(weights, head2head):
    info = []
    w = len(weights)
    for p in range(w):
        high = [i for i in range(w) if weights[i]>weights[p]] # 더 무거운 사람 인덱스
        over = len([info for info in high if head2head[p][info]=="W"]) # 더 무거운 사람 이긴 수
        rate = 0 if not (w-head2head[p].count("N")) else head2head[p].count("W")/(w-head2head[p].count("N"))
        info.append((p, weights[p], rate, over)) # 번호, 자기무게, 승률, 무거운복서 이긴 횟수
    info = sorted(info, key=lambda x: (x[2], x[3], x[1], -x[0]), reverse=True)
    return [num[0]+1 for num in info]
