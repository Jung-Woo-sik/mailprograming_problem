from collections import defaultdict, deque

def solution(game_board, table):
    answer = 0
    N = len(game_board)
    visit, visit2 = defaultdict(int), defaultdict(int)
    queue, queue2 = deque(), deque()
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    piece, piece2 = [], []
        
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                if visit[(i, j)] == 0:
                    l, t, r, b = i, j, i, j
                    visit[(i, j)] = 1
                    queue.append([i, j])
                    count = 1
                    
                    while queue:
                        x, y = queue.popleft()
                        
                        for d1, d2 in d:
                            if 0 <= x + d1 < N and 0 <= y + d2 < N and game_board[x + d1][y + d2] == 0 and visit[(x + d1, y + d2)] == 0:
                                queue.append([x + d1, y + d2])
                                l = min(l, x + d1)
                                t = min(t, y + d2)
                                r = max(r, x + d1)
                                b = max(b, y + d2)
                                visit[(x + d1, y + d2)] = 1
                                count += 1
                    
                    piece.append([l, t, r, b, count])
            
            if table[i][j] == 1:
                if visit2[(i, j)] == 0:
                    l, t, r, b = i, j, i, j
                    visit2[(i, j)] = 1
                    queue2.append([i, j])
                    count = 1
                    
                    while queue2:
                        x, y = queue2.popleft()
                        
                        for d1, d2 in d:
                            if 0 <= x + d1 < N and 0 <= y + d2 < N and table[x + d1][y + d2] == 1 and visit2[(x + d1, y + d2)] == 0:
                                queue2.append([x + d1, y + d2])
                                l = min(l, x + d1)
                                t = min(t, y + d2)
                                r = max(r, x + d1)
                                b = max(b, y + d2)
                                visit2[(x + d1, y + d2)] = 1
                                count += 1
                    
                    piece2.append([l, t, r, b, count])
    
    for l, t, r, b, count in piece:
        for l2, t2, r2, b2, count2 in piece2:
            A = [row[t:b+1] for row in game_board[l:r+1]]
            B = [row[t2:b2+1] for row in table[l2:r2+1]]
            
            if count == count2:
                c = 0
                T = False
                
                while c < 4 and not T:
                    c += 1
                    n = len(A)
                    m = len(A[0])
                    
                    if n == len(B) and m == len(B[0]):
                        for i in range(n):
                            for j in range(m):
                                if A[i][j] + B[i][j] != 1: break

                                if i == n - 1 and j == m - 1:
                                    T = True
                                    break

                            if A[i][j] + B[i][j] != 1 or T: break
                    
                    B = rotate90(B)
            
                if T:
                    answer += count
                    piece2.remove([l2, t2, r2, b2, count2])
                    break
        
    return answer
        
def rotate90(key):
    n = len(key)
    m = len(key[0])
    
    key_ = [[0] * n for i in range(m)]
    
    for i in range(n):
        for j in range(m):
            key_[j][n-i-1] = key[i][j]
    
    return key_
    
    print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]])) # 14
