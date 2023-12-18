def split_beam(direction, splitter):
    if splitter == '|':
        return ['up', 'down'] if direction in ['right', 'left'] else [direction]
    else:  # Splitter is '-'
        return ['right', 'left'] if direction in ['up', 'down'] else [direction]


def trace_beam(grid, start_pos, start_dir):
    energized = set()
    tested = set()
    paths = [(start_pos, start_dir)]

    while paths:
        (x, y), direction = paths.pop(0)  # Using queue behavior
        dx, dy = directions[direction]

        while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            current_tile = grid[x][y]
            energized.add((x, y))
            if ((x, y), direction) in tested:
                break
            tested.add(((x, y), direction))

            if current_tile in reflections:
                # Change direction based on the mirror
                direction = reflections[current_tile][direction]
                dx, dy = directions[direction]

            elif current_tile in '|-':
                # Split the beam
                new_directions = split_beam(direction, current_tile)
                for new_dir in new_directions:
                    ndx, ndy = directions[new_dir]
                    paths.append(((x + ndx, y + ndy), new_dir))
                break  # Exit the current path after splitting

            # Move to the next tile in the current direction
            x, y = x + dx, y + dy

    return len(energized)


directions = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
}

reflections = {
    '/': {'right': 'up', 'down': 'left', 'left': 'down', 'up': 'right'},
    '\\': {'right': 'down', 'down': 'right', 'left': 'up', 'up': 'left'}
}

with open('data.txt') as f:
    grid = [line.strip('\n') for line in f.readlines()]

# Task 2
largest = 0
for i in range(len(grid[0])):
    energized = trace_beam(grid, (0, i), 'down')
    if energized > largest:
        largest = energized
    energized = trace_beam(grid, (len(grid) - 1, i), 'up')
    if energized > largest:
        largest = energized
for i in range(len(grid[0])):
    energized = trace_beam(grid, (i, 0), 'right')
    if energized > largest:
        largest = energized
    energized = trace_beam(grid, (i, len(grid[0]) - 1), 'left')
    if energized > largest:
        largest = energized
print(largest)

# Task 1
energized_tiles = trace_beam(grid, (0, 0), 'right')
print(energized_tiles)
