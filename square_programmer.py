import math
def solution(w,h):
    answer = 1
    return w*h - (w+h - math.gcd(w,h)) # 최대공약수가 가로세로 겹치는부분임으로 빼야함
