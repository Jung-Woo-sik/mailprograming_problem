def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:#progress를 큐로 사용
        if (progresses[0] + time*speeds[0]) >= 100: #시간 * 스피드 + 프로그레스가 100이상이면 0번째 자리를 비우고 카운트 증가 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:#그렇지 않을경우 카운트의 갯수를 answer에 append하고 count 초기화 
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


