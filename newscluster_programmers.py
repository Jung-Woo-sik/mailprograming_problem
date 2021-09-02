from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower() #str1 과 str2 형식을 맞추기 위해 소문자로 변경
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):#알파벳 형식이면 2자씩 묶어줌
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])

    Counter1 = Counter(str1_lst)#만든 리스트를 카운터 형식으로 변경
    Counter2 = Counter(str2_lst)    
    
    inter = list((Counter1 & Counter2).elements())#교집합 합집합 구하기
    union = list((Counter1 | Counter2).elements())
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
