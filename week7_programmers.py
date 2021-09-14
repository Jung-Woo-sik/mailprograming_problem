def solution(enter, leave):
    answer = [[] for _ in range(len(enter)+1)]
    room = []
    ei, li = 0, 0#enter와 leave의 포인터
    while ei<len(enter) or li<len(leave): # ei와 li가 리스트를 벗어나지 않도록 설정
        if leave[li] not in room:#사람이 입장할 때 answer에 현재 room에 있던 인원을 저장한다
            answer[enter[ei]]=room[:]
            room.append(enter[ei])
            ei += 1
        else:
            room.remove(leave[li])
            li += 1
    for p, person in enumerate(answer): #  회의실에 입장했을 당시 회의실에 있던 사람들이 저장
        for met in person:
            answer[met].append(p)
    return [len(set(i)) for i in answer][1:] # answer에는 각자 마주친 사람의 번호가 저장된 리스트가 저장 set으로 중복 제거