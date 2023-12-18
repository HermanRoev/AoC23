def rotate_matrix_90_degrees(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def move_zeros(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    for i in range(num_columns):
        top = 0
        for j in range(num_rows):
            if matrix[j][i] == 'O':
                matrix[j][i] = '.'
                matrix[top][i] = 'O'
                top += 1
            elif matrix[j][i] == '#':
                top = j + 1
    return matrix


def find_sum(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    sum = 0

    for i in range(num_columns):
        for j in range(num_rows):
            if matrix[j][i] == 'O':
                sum += 100 - j

    return sum


def matrix_state_with_direction(matrix, direction):
    matrix_str = '\n'.join(''.join(row) for row in matrix)
    return f"{matrix_str}|{direction}"


def move_zeros_and_calculate_sum(text_lines, cycles):
    matrix = [list(line.strip()) for line in text_lines]

    seen_states = set()
    directions = ['up', 'left', 'down', 'right']

    for i in range(cycles):
        direction = directions[i % 4]
        matrix = move_zeros(matrix)
        matrix = rotate_matrix_90_degrees(matrix)

        # Convert the matrix to a string with direction and check for repetition
        state = matrix_state_with_direction(matrix, direction)
        if state not in seen_states:
            seen_states.add(state)

    return find_sum(matrix)


# Read the file and run the process
with open('input.txt', 'r') as f:
    data = f.readlines()

# Check for repeating patterns in 4,000,000,000 cycles
total_sum = move_zeros_and_calculate_sum(data, 4000)
print(total_sum)
