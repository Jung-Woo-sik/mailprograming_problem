def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
    ans = 0
    for x in win_nums: #lottos 에서 win_num 개수 체크
        if x in lottos:
            ans += 1
             
    return rank[cnt_0 + ans],rank[ans] #0개수 +win_num, winnum에 맞는 등수


