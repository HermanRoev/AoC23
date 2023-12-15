
def check_if_faster(time, distance):
    faster = []
    for i in range(time):
        new_distance = i*(time-i)
        if new_distance > distance:
            faster.append(i)
    return faster


def calculate_faster_times(time, distance):
    time_list = check_if_faster(time, distance)
    return len(time_list)


def calculate_answer(time_list):
    answer = 1
    for time in time_list:
        answer *= len(time)
    return answer


times = 46689866
distance = 358105418071080

print(calculate_faster_times(times, distance))
