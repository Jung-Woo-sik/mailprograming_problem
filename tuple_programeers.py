def solution(s):
    answer = []
    s = s[2:-2]#양끝 {}제거
    s = s.split("},{")
    s.sort(key = len)#길이별 정리
    for i in s:
        ii = i.split(',') #","으로 split
        for j in ii:
            if int(j) not in answer: #answer에 없으면 append
                answer.append(int(j))
    return answer


"""
import re
 
def solution(s):#정규 표현식을 활용한 풀이법
    answer = []
    a = s.split(',{')
    a.sort(key = len)
    for j in a:
        numbers = re.findall("\d+", j) #숫자를 리스트로 반환
        for k in numbers:
            if int(k) not in answer:
                answer.append(int(k))
    return answer

"""
