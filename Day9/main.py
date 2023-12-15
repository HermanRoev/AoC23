def load_input(input):
    with open(input) as f:
        return [[int(num) for num in line.strip().split()] for line in f.readlines()]


def find_sequences(input):
    memory = []
    current = input

    memory.append(current)
    while any(current):
        current = find_sequence(current)
        memory.append(current)
    return memory


def find_sequence(input):
    history = []
    for i in range(len(input)-1, 0, -1):
        history.insert(0, input[i]-input[i-1])
    return history


def calculate_sum(input):
    sum = 0
    for line in input:
        history = find_sequences(line)
        sum += calculate_next(history)

    return sum


def calculate_next(input):
    next_value = input[-1][0]

    for step in reversed(input):
        next_value = step[0] - next_value

    return next_value


def main():
    input = load_input('input.txt')
    sum = calculate_sum(input)
    print(sum)


if __name__ == '__main__':
    main()