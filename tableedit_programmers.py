def solution(n, k, cmd):#stack을 만들어서 stack pointer를 움직이면서 해결
    exists = [True for _ in range(n)]
    up = [-1] + [x for x in range(n - 1)]
    down = [x for x in range(1, n)] + [-1]
    deleted = []
    
    for c in cmd:
        op = c[0]
        
        if op == 'U':#up
            val = int(c.split()[1])
            for _ in range(val):
                k = up[k]
                
        elif op == 'D':#down
            val = int(c.split()[1])
            for _ in range(val):
                k = down[k]
                
        elif op == 'C':#choice
            if up[k] != -1:
                down[up[k]] = down[k]
            if down[k] != -1:
                up[down[k]] = up[k]
            exists[k] = False
            deleted.append(k)
            k = down[k] if down[k] != -1 else up[k]
            
        elif op == 'Z':# ctrl Z
            d = deleted.pop()
            if up[d] != -1:
                down[up[d]] = d
            if down[d] != -1:
                up[down[d]] = d
            exists[d] = True
            
        else:
            raise RuntimeError(op)
    
    return ''.join(['O' if x else 'X' for x in exists])
