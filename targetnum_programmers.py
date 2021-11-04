from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    print(n)
    queue.append([numbers[0],0])
    print(queue)
    queue.append([-1*numbers[0],0])
    print(queue)

    while queue:
        temp, idx = queue.popleft()
        print(temp,idx)
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
            print(queue)
        else:
            if temp == target:
                answer += 1
    return answer