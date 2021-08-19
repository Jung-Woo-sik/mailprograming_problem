def solution(lines):
    answer = 0
    total_times = []
    for i in range(len(lines)):
        start_time, end_time = get_times(lines[i])
        total_times.append((start_time, end_time, i))

    for i in range(len(total_times)):
        count = 1
        end_time = total_times[i][1]
        for j in range(len(total_times)):
            if i == j:
                continue
            t_start_time = total_times[j][0]
            t_end_time = total_times[j][1]
            if t_start_time >= end_time and t_start_time < end_time + 1000:
                count += 1
            elif t_end_time >= end_time and t_end_time < end_time + 1000:
                count += 1
            elif end_time >= t_start_time and end_time + 1000 <= t_end_time:
                count += 1
        if count > answer:
            answer = count

    return answer


def get_times(log):
    temp = log.split(" ")
    end_time = temp[1].split(':')
    end_time = int(end_time[0]) * 3600000 + int(end_time[1]) * 60000 + int(end_time[2].replace('.', ''))
    start_time = end_time - int(float(temp[2].replace('s', ''))*1000) + 1
    return (start_time, end_time) if start_time > 0 else (0, end_time)
