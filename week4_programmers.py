def solution(table, languages, preference):
    answer = []
    new_table = sorted([list(t.split()) for t in table], key=lambda x : x[0])
    #table을 2차원 배열로 사용
    job = {n: new_table[n][0] for n in range(len(new_table))}
    #table의 직업을 0부터 5의 딕셔너리로 만듬
    for j in range(len(job)):#lang과 pref를 zip하여 
        total = 0
        for lang, pref in zip(languages, preference):
            if lang in new_table[j]:
                total += (6 - new_table[j].index(lang)) * pref#table index는 점수와 반대임으로 6에서 마이너스하여 사용
        answer.append(total)
        
    return job[answer.index(max(answer))] #index의 job을 리턴
