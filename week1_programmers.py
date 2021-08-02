def solution(price, money, count):
    answer = -1
    x = count * (count + 1) // 2
    sum_price = price * x
    if money > sum_price:
        answer = 0
    else:
        answer = sum_price-money
    return answer
