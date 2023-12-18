
directions = {"R" : (1, 0), "L" : (-1, 0), "U" : (0, 1), "D" : (0, -1)}

with (open("input.txt") as f):
    data = [[part for part in line.strip().split()] for line in f.readlines()]


coordinates = [(0, 0)]
for entry in data:
    direction = entry[0]
    steps = int(entry[1])
    for i in range(steps):
        x, y = coordinates[-1]
        coordinates.append((x + directions[direction][0], y + directions[direction][1]))


# Initialize min_x and min_y to positive infinity
min_x = float('inf')
min_y = float('inf')

# Reuse the previous max_x and max_y initializations
max_x = float('-inf')
max_y = float('-inf')

# Iterate through each tuple
for x, y in coordinates:
    # Update max_x and max_y if current values are greater
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    # Update min_x and min_y if current values are smaller
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y


dot_array = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

for x, y in coordinates:
    dot_array[y + abs(min_y)][x + abs(min_x)] = '#'


stack = [(84, 84)]
while stack:
    x, y = stack.pop()
    # Check boundaries and whether the position should be filled
    if 0 <= x < len(dot_array[0]) and 0 <= y < len(dot_array) and dot_array[y][x] != "#" and dot_array[y][x] != '#':
        dot_array[y][x] = '#'
        # Add adjacent positions to the stack
        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))


# Write the dot array to the specified file
with open('array.txt', 'w') as file:
    for row in dot_array:
        file.write(''.join(row) + '\n')

sum = 0
for row in dot_array:
    sum += row.count('#')

print('Part 1:', sum)


# Part 2
direction_dict = {0 : 'R', 1 : 'D', 2 : 'L', 3 : 'U'}

dig_plan = []
for entry in data:
    hex = entry[2]
    steps, direction = hex[2:-2], hex[-2]
    steps = int(steps, 16)
    direction = direction_dict[int(direction)]
    dig_plan.append((direction, steps))

points = [(1, 1)]
perimeter = 0
for dir, dist in dig_plan:
    perimeter += dist
    # Move from the last point in the specified direction
    points.append((points[-1][0] + dist * directions[dir][0], points[-1][1] + dist * directions[dir][1]))

result = 0
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    result += x1 * y2 - x2 * y1
result = abs(result) // 2

print('Part 2:', result + perimeter // 2 + 1)
