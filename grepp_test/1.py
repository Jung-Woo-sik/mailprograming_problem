def solution(infos, actions):
    answer = []
    login = False
    cart = False
    for i in actions:
        x = i.split(" ")
        if x[0] == 'ADD':
            answer.append(login)
            cart = True
        elif x[0] == 'LOGIN':
            if login == True:
                answer.append(False)
            else:
                for j in infos:
                    y = j.split(' ')
                    if y[0] == x[1]:
                        if y[1] == x[2]:
                            login = True
                            break
                answer.append(login)
        elif x[0] == 'ORDER':
            if login == True and cart == True:
                cart = False
                answer.append(True)
            else:
                answer.append(False)
    return answer