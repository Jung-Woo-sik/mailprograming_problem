def solution(scores):
    answer = ''
    cnt = len(scores)
    for i in range(cnt):
        cur = []
        
        for idx in range(cnt):
            score = scores[idx][i]
            cur.append(score)
            
        max_score = max(cur)
        min_score = min(cur)
        max_cnt = cur.count(max_score)
        min_cnt = cur.count(min_score)
        
        self_score = cur[i]
        sum_score = sum(cur)
        cnt_score = len(cur)
        
        if max_score == self_score and max_cnt == 1:
            sum_score = sum_score - self_score
            cnt_score = cnt_score -1
        elif min_score == self_score and min_cnt == 1:
            sum_score = sum_score - self_score
            cnt_score = cnt_score -1
            
        avg = sum_score / cnt_score
        
        if avg >= 90:
            answer = answer + 'A'
        elif 80 <= avg <90:
            answer = answer + 'B'
        elif 70 <= avg < 80:
            answer = answer + 'C'
        elif 50 <= avg < 80:
            answer = answer + 'D'
        else:
            answer = answer +'F'
    return answer
