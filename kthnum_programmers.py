def solution(array, commands):
    answer = []
    #x = array[int(commands[0]):int(commands[1])]
    #print(x)
    
    for i in commands:
        x = array[int(i[0])-1:int(i[1])]
        a = sorted(x)
        s = int(i[2])
        answer.append(a[s-1])
    return answer
