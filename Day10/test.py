def create_map(input):
    return [list(line) for line in input.splitlines()]


def find_start(map):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == 'S':
                return i, j


def find_first_pipe(map, start):
    rows, cols = len(map), len(map[0])
    x, y = start
    connected_pipes = []
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    pipe_connections = {
        '|': ['N', 'S'],  # Accessible from North or South
        '-': ['E', 'W'],  # Accessible from East or West
        'L': ['S', 'W'],  # Accessible from South or West
        'J': ['S', 'E'],  # Accessible from South or East
        '7': ['N', 'E'],  # Accessible from North or East
        'F': ['N', 'W']   # Accessible from North or West
    }

    # Check each direction
    for dir, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            pipe_at_next = map[nx][ny]
            if pipe_at_next in pipe_connections and dir in pipe_connections[pipe_at_next]:
                connected_pipes.append(((nx, ny), pipe_at_next, dir))

    return connected_pipes


def traverse_loop(map, pos, from_direction, visited=None):
    if visited is None:
        visited = []

    directions = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
    next_steps = {'|': {'N': ('S', 1, 0), 'S': ('N', -1, 0)},
                  '-': {'W': ('E', 0, 1), 'E': ('W', 0, -1)},
                  'L': {'N': ('E', 0, 1), 'E': ('N', -1, 0)},
                  'J': {'N': ('W', 0, -1), 'W': ('N', -1, 0)},
                  '7': {'S': ('W', 0, -1), 'W': ('S', 1, 0)},
                  'F': {'S': ('E', 0, 1), 'E': ('S', 1, 0)}}

    while True:
        if pos in visited:
            break

        x, y = pos
        pipe = map[x][y]
        visited.append((pos, pipe))

        if pipe == 'S':
            break

        entry_direction = directions[from_direction]

        next_dir, dx, dy = next_steps[pipe][entry_direction]
        pos = (x + dx, y + dy)
        from_direction = next_dir

    return visited


def final_scanline_count_enclosed_tiles(map, loop_positions):

    rows, cols = len(map), len(map[0])
    enclosed_tiles = 0
    inside_loop = False
    loop_info = {pos: pipe for pos, pipe in loop_positions}

    for i in range(rows):
        for j in range(cols):
            if (i, j) in loop_info:
                pipe = loop_info[(i, j)]
                if pipe == 'F':
                    j += 1
                    next_tile = loop_info.get((i, j))
                    while next_tile == '-':
                        j += 1
                        next_tile = loop_info.get((i, j))
                    if next_tile == 'J' or next_tile == 'S':
                        inside_loop = not inside_loop
                if pipe == 'L':
                    j += 1
                    next_tile = loop_info.get((i, j))
                    while next_tile == '-':
                        j += 1
                        next_tile = loop_info.get((i, j))
                    if next_tile == '7':
                        inside_loop = not inside_loop
                if pipe == '|':
                    inside_loop = not inside_loop
            elif inside_loop:
                enclosed_tiles += 1

    return enclosed_tiles


with open('input.txt') as f:
    map = create_map(f.read())
    start = find_start(map)
    connected_pipes = find_first_pipe(map, start)
    loop_positions = traverse_loop(map, connected_pipes[0][0], connected_pipes[0][2])
    print(f'Loop length: {len(loop_positions)}')
    enclosed_tiles = final_scanline_count_enclosed_tiles(map, loop_positions)
    print(f'Enclosed tiles: {enclosed_tiles}')