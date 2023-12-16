def split_beam(direction, splitter):
    if splitter == '|':
        return ['up', 'down'] if direction in ['right', 'left'] else ['right', 'left']
    else:  # Splitter is '-'
        return ['right', 'left'] if direction in ['up', 'down'] else ['up', 'down']


def trace_beam(grid, start_pos, start_dir):
    energized = set()
    path = [(start_pos, start_dir)]

    while path:
        (x, y), direction = path.pop()
        dx, dy = directions[direction]

        while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y] in reflections:
                direction = reflections[grid[x][y]][direction]
                break
            elif grid[x][y] in '|-':
                path.extend([(x, y), new_dir] for new_dir in split_beam(direction, grid[x][y]))
                break
            energized.add((x, y))
            x, y = x + dx, y + dy

    return energized


def count_energized_tiles(grid):
    start_pos = (0, 0)  # Top-left corner
    start_dir = 'right'
    energized = trace_beam(grid, start_pos, start_dir)
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

energized_tiles = count_energized_tiles(grid)
print(energized_tiles)
