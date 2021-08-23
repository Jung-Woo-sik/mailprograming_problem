score = {"A+" : 0,"A0" : 1,"A-" : 2,"B+" : 3,
    "B0" : 4,"B-" : 5,"C+" : 6,
    "C0" : 7,"C-" : 8,"D+" : 9,
    "D0" : 10,"D-" : 11,"F" : 12}

def solution(grades):
    answer = []
    grade = []
    subject = []
    for i in grades:
        x = i.split(' ')
        grade.append(x[1])
        subject.append(x[0])
    x = []
    for i in subject:
        #print(i)
        for j in range(0,len(subject)):
            if i == subject[j]:
                x.append(j)
        #if len(x)>=1:
        y = find(x,grade)
        #else:
        #    y = x[0]
       # print(y)
        #print(y)
        x = []
        answer.append(y)
    ans = set(answer)
    sort_ans = sorted(ans,key = lambda ans : score[grade[ans]])
    real_ans = []
    for i in sort_ans:
        real_ans.append(grades[i])
    return real_ans

def find(x,grade):

    
    maxValue = x[0]
    
    for i in range(1,len(x)):
        if score[grade[maxValue]] > score[grade[x[i]]]:
            maxValue = x[i]
    return maxValue