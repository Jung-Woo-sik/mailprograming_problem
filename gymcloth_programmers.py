def solution(n, lost, reserve):
    reser_del = set(reserve)-set(lost)#서로 중복 될 수 없다 명시했으나 혹시 모를 경우 제거
    lost_del = set(lost)-set(reserve)
    
    for i in reser_del:#여벌 옷이 있는 학생으로 없는 학생을 하나씩 제거
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)
    
    return n-len(lost_del) #전체에서 옷이 없는 학생 빼서 리턴

