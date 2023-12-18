from collections import defaultdict

#Task 1
def load_data(data):
    with open(data, 'r') as f:
        data = f.read().strip()
    return [x for x in data.split(',')]


def hash_data(data):
    value = 0
    for char in data:
        value += ord(char)
        value *= 17
        value %= 256
    return value


#Task 2
def split_data(data):
    char, value = data.split('=' if '=' in data else '-')
    return char, value


def hasmap(data):
    map = defaultdict(list)
    for entry in data:
        char, value = split_data(entry)
        hash_value = hash_data(char)
        if value:
            fist = map[hash_value]
            for i in range(len(fist)):
                if fist[i][0] == char:
                    fist[i] = (char, value)
                    break
            else:
                map[hash_data(char)].append((char, value))
        else:
            fist = map[hash_value]
            for i in range(len(fist)):
                if fist[i][0] == char:
                    fist.pop(i)
                    break
    return map


def calculate_focusing_power(map):
    power = 0
    for key in map:
        for i in range(len(map[key])):
            power += (i+1) * int(map[key][i][1]) * (key+1)
    return power


data = load_data('verification.txt')
map = hasmap(data)
focal_power = calculate_focusing_power(map)
print('Task 2: ', focal_power)

sum = 0
for entry in data:
    sum += hash_data(entry)
print('Task 1: ', sum)
