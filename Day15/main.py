def load_data(data):
    with open(data, 'r') as f:
        data = f.read().strip()
    return [x for x in data.split(',')]


def hash_data(data):
    sum = 0
    for enrty in data:
        value = 0
        for char in enrty:
            value += ord(char)
            value *= 17
            value %= 256
        sum += value
    return sum


data = load_data('verification.txt')
sum = hash_data(data)
print(sum)