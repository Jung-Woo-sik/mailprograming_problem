def solution(answers): 
    answer = [] 
    tester_1 = [1, 2, 3, 4, 5] 
    tester_2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    tester_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    len_tester_1 = len(tester_1) 
    len_tester_2 = len(tester_2) 
    len_tester_3 = len(tester_3) 
    check_1 = 0 
    check_2 = 0 
    check_3 = 0 
    for i in range(len(answers)): 
        if tester_1[i%len_tester_1] == answers[i]: 
            check_1 = check_1 + 1 
        if tester_2[i%len_tester_2] == answers[i]: 
            check_2 = check_2 + 1 
        if tester_3[i%len_tester_3] == answers[i]: 
            check_3 = check_3 + 1 
    max_right = max(check_1, check_2, check_3) 
    if max_right == check_1: 
        answer.append(1) 
    if max_right == check_2: 
        answer.append(2) 
    if max_right == check_3: 
        answer.append(3) 
    answer = sorted(answer) 
    return answer
