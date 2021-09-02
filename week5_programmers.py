def solution(word):
    answer = len(word)
    word_dict = {'A':0,'E':1,'I':2,'O':3,'U':4}
    re = (((5 + 1)*5 + 1)*5 + 1)*5 + 1
    for i in word:
        answer += re * word_dict[i]
        re = (re - 1) // 5

    return answer
