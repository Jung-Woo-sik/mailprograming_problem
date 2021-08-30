def solution(s): 
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)#stack이 비었다 = 초기상태 or 합쳐져서 pop됨
        elif stack[-1] == i: stack.pop()#stack의 top과 i를 비교해서 같으면 stack pop
        else: stack.append(i)
    if len(stack) == 0: return 1 #stack이 존재하면 0 없으면 1 return
    else: return 0
