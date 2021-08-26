def solution(record):
    answer = []
    userdict = {}
    
    for mes in record:#record 에서 dictionary로 만들기 id당 닉네임으로 바꿔준다
        if (mes.split(' ')[0] == 'Enter') or (mes.split(' ')[0] == 'Change'):
            userdict[mes.split(' ')[1]] = mes.split(' ')[2]
    for mes in record: record당 enter leave를 id별로 닉네임을 매치시켜준다.
        if mes.split(' ')[0] == 'Enter': 
            answer.append("{}님이 들어왔습니다.".format(userdict[mes.split(' ')[1]]))
        elif mes.split(' ')[0] == 'Leave': 
            answer.append("{}님이 나갔습니다.".format(userdict[mes.split(' ')[1]]))
        else:
            pass

            
    return answer
