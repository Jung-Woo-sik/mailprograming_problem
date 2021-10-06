def solution(n, wires):

    def find(f,x):
        if f[x] == x:
            return x
        
        f[x] = find(f,f[x])
        return f[x]
        
    def union(f,a,b):
        
        a = find(f,a)
        b = find(f,b)
        
        if f[a] == f[b]:
            return 
        
        elif a < b:
            f[b] = a
            
        elif b < a:
            f[a] = b
    
    answer_list = []
    
    for i in range(n-1):
        f = [k for k in range(n+1)]   # parent 생성
        print(f)
        for j in range(n-1):
            if i == j: continue  # 한개씩 빼봄
            a,b = wires[j][0],wires[j][1]
            union(f,a,b)    # union
        
        for m in range(1,n+1): # 최종 갱신
            find(f,m)
        one = f.count(1)
        two = n-one
    
        answer_list.append(abs(one-two))
    
    
    return min(answer_list)