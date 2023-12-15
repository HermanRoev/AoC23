
def create_map(input):
    map = [[symbol for symbol in line] for line in input.splitlines()]
    return map


def find_start(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'S':
                return i, j


def find_first_pipe(map, start):
    rows, cols = len(map), len(map[0])
    x, y = start
    connected_pipes = []

    # Check each direction: North, South, East, West
    if x > 0 and map[x-1][y] in ["|", "F", "7"]:  # North
        connected_pipes.append(((x-1, y), map[x-1][y]))
    if x < rows - 1 and map[x+1][y] in ["|", "L", "J"]:  # South
        connected_pipes.append(((x+1, y), map[x+1][y]))
    if y > 0 and map[x][y-1] in ["-", "L", "F"]:  # West
        connected_pipes.append(((x, y-1), map[x][y-1]))
    if y < cols - 1 and map[x][y+1] in ["-", "7", "J"]:  # East
        connected_pipes.append(((x, y+1), map[x][y+1]))

    return connected_pipes


def traverse_loop(map, pos, from_direction, visited=None):
    if visited is None:
        visited = set()

    while True:
        if pos in visited:  # Avoid revisiting the same pipe
            break

        visited.add(pos)
        x, y = pos
        pipe = map[x][y]

        if pipe == 'S':  # End of loop
            break

        entry_direction = None
        # Flip the direction to represent entry from the perspective of the next pipe
        if from_direction == 'north':
            entry_direction = 'south'
        elif from_direction == 'south':
            entry_direction = 'north'
        elif from_direction == 'east':
            entry_direction = 'west'
        elif from_direction == 'west':
            entry_direction = 'east'

            # Determine the next position and direction based on the current pipe
        next_pos = None
        next_direction = None

        if pipe == '|':
            if entry_direction == 'south':
                next_pos = (x - 1, y)
                next_direction = 'north'
            elif entry_direction == 'north':
                next_pos = (x + 1, y)
                next_direction = 'south'

        elif pipe == '-':
            if entry_direction == 'west':
                next_pos = (x, y + 1)
                next_direction = 'east'
            elif entry_direction == 'east':
                next_pos = (x, y - 1)
                next_direction = 'west'

        elif pipe == 'L':
            if entry_direction == 'north':
                next_pos = (x, y + 1)
                next_direction = 'east'
            elif entry_direction == 'east':
                next_pos = (x - 1, y)
                next_direction = 'north'

        elif pipe == 'J':
            if entry_direction == 'north':
                next_pos = (x, y - 1)
                next_direction = 'west'
            elif entry_direction == 'west':
                next_pos = (x - 1, y)
                next_direction = 'north'

        elif pipe == '7':
            if entry_direction == 'south':
                next_pos = (x, y - 1)
                next_direction = 'west'
            elif entry_direction == 'west':
                next_pos = (x + 1, y)
                next_direction = 'south'

        elif pipe == 'F':
            if entry_direction == 'south':
                next_pos = (x, y + 1)
                next_direction = 'east'
            elif entry_direction == 'east':
                next_pos = (x + 1, y)
                next_direction = 'south'

        if next_pos is None or next_direction is None:
            return 0  # End of path or invalid path

        pos = next_pos
        from_direction = next_direction

    return visited


with open('input.txt') as f:
    input = f.read()
    map = create_map(input)
    start = find_start(map)
    connected_pipes = find_first_pipe(map, start)
    loop_length = traverse_loop(map, connected_pipes[0][0], 'north')
    print(f'Loop length: {len(loop_length)}')