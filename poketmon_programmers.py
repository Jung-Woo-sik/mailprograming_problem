def solution(nums):
    answer = 0
    a = set(nums);
    if len(nums)/2 <len(a):
        answer = len(nums)/2
    else:
        answer = len(a)
    return answer
