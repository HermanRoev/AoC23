
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


# Task 1 & 2
def calculate_distance_with_expansion(lines, num_duplicates):
    height = len(lines)
    length = len(lines[0])

    # Find empty rows and columns
    empty_rows = [i for i in range(height) if all(char == '.' for char in lines[i])]
    empty_columns = [i for i in range(length) if all(lines[j][i] == '.' for j in range(height))]

    # Find coordinates of non-empty points
    coordinates = [(x, y) for y in range(height) for x in range(length) if lines[y][x] == '#']

    # Calculate adjusted distances
    distance = 0
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            dx = abs(coordinates[i][0] - coordinates[j][0])
            dy = abs(coordinates[i][1] - coordinates[j][1])

            # Add distances for empty columns
            for k in range(min(coordinates[i][0], coordinates[j][0]), max(coordinates[i][0], coordinates[j][0])):
                if k in empty_columns:
                    dx += num_duplicates

            # Add distances for empty rows
            for k in range(min(coordinates[i][1], coordinates[j][1]), max(coordinates[i][1], coordinates[j][1])):
                if k in empty_rows:
                    dy += num_duplicates

            distance += dx + dy

    return distance


# Call the function with your input lines
distance = calculate_distance_with_expansion(lines, 1)
print(f'Task 1: {distance}')
distance = calculate_distance_with_expansion(lines, 999_999)
print(f'Task 2: {distance}')
