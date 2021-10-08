def make_trie(words):
    dic = {}
    for word in words:
        current_dict = dic
        for letter in word:
            current_dict.setdefault(letter, [0, {}])
            current_dict[letter][0] +=1              
            current_dict = current_dict[letter][1]

    return dic

def solution(words):
    answer = 0
    trie = make_trie(words)
    for word in words:
        temp = trie
        for letter in word:
            answer += 1
            temp = temp[letter]
            if temp[0] == 1:
                break
            else:
                temp = temp[1]
    
    return answer