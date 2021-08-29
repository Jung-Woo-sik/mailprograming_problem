from collections import deque


def solution(n, edge):
    answer = 0
    route = [0]*(n+1) #노드 1부터 각 노드까지의 거리
    edge.sort() #노드 1부터 연결 정보 확인하기 위해 정렬
    queue = deque() 
    graph = [[] for i in range(n+1)] #각 노드에 연결된 노드 정보 저장
    
    for e in edge: # 양방향이므로 
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    queue.append(1)
    route[1] = 1
    
    while queue:
        now = queue.popleft()
        for g in graph[now]:
            if route[g]==0:
                queue.append(g)
                route[g] = route[now]+1
        
    # 1번 노드로부터 가장 멀리 떨어진 노드 개수 계산
    max_edge= max(route)
    for r in route:
        if r == max_edge:
            answer+=1     
            
    return answer

