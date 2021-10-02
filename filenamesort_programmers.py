import re
def solution(files):
    answer = []
    temp = [re.split(r"(\d+)",s)for s in files]#숫자를 기준으로 스플릿
    
    sort = sorted(temp,key = lambda x: (x[0].lower(),int(x[1])))#x[0]를 첫번째 기준 x[1]을 두번째 기준으로 정렬

    return ["".join(s) for s in sort]