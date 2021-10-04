def solution(sizes):
    W,H=0,0#w = 큰것중 가장 큰값 h = 작은것중 가장 큰 값
    for w,h in sizes: W,H=max(W,w,h),max(H,min(w,h))
    return W*H