def move_zeros(text_lines):
    matrix = [list(line.strip()) for line in text_lines]
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
                top = j+1
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


with open('input.txt', 'r') as f:
    data = f.readlines()

processed_lines = move_zeros(data)
sum = find_sum(processed_lines)
print(sum)
