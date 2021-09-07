from itertools import permutations

def isMatch(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i])!=len(banned_set[i]):#길이가 다르면 false
            return False
        for j in range(len(user_set[i])):
            if banned_set[i][j]=='*':#*이면 비교를 계속함
                continue
            if user_set[i][j]!=banned_set[i][j]:#한글자라도 다르면 false
                return False
    return True
    
def solution(user_id, banned_id):
    ans=[]
    for com_set in permutations(user_id, len(banned_id)):#배열에서 숫자만큼의 순열 ex)[a,b,c],2 == [a,b],[a,c],[b,c] 
        if isMatch(com_set, banned_id):
            com_set = set(com_set) # 중복 제거
            if com_set not in ans:
                ans.append(com_set)
    return len(ans)


