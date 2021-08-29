def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    
    for t1, t2 in tickets:# ticket 기반으로 route dict 채우기
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    
    st = ['ICN']
    ans = []
    
    while st:
        top = st[-1]#st의 마지막 요소를 top으로
        if top not in routes or len(routes[top])==0: # route에 top이 없거나 routes[top]에 아무것도 없을때
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
        print(ans,st)
    ans.reverse()
    
    return ans
