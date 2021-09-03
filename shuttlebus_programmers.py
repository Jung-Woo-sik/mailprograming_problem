def solution(n, t, m, timetable):
    answer = ''
    crew = [ int(tt.split(":")[0])*60+int(tt.split(":")[1]) for tt in timetable ] #시간문제가 나올시 가장 작은 단위로 변환
    # 크루의 도착시간
    crew.sort()

    # bus[x] = (버스시간, 승객 수, 마지막 탄 크루의 도착시간)
    bus = [ (540+t*i, 0, None) for i in range(n)]

    bidx, cidx = 0, 0
    while cidx < len(crew):
        c = crew[cidx]
        if bidx == len(bus):
            break
        if c <= bus[bidx][0] and bus[bidx][1] < m:
            tt, cnt, _ = bus[bidx]
            bus[bidx] = (tt, cnt+1, c)
            cidx += 1
        else:
            bidx += 1

    ret = bus[-1][0]
    if bus[-1][2]:
        if bus[-1][1] == m:
            ret = bus[-1][2] - 1

    return '%02d:%02d' % (ret // 60, ret % 60)
