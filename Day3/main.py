def sum_part_numbers(data):
    sum_of_parts = 0
    symbols = set("*#$%&/=+-@$")  # Define the symbols you consider as valid

    # Convert the string data into a grid (2D list)
    grid = [list(line) for line in data]

    # Function to check for symbols around the number
    def is_adjacent_to_symbol(x, y, z, grid):
        # Check adjacent cells in the grid
        while y <= z:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                        if grid[x + dx][y + dy] in symbols:
                            return True
            y += 1
        return False

    # Iterate over each character in the grid
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j].isdigit():
                # If the current character is a digit, check if it's part of a number
                number = grid[i][j]
                k = j + 1
                # Construct the full number
                while k < len(grid[i]) and grid[i][k].isdigit():
                    number += grid[i][k]
                    k += 1

                # Check if this number is adjacent to a symbol
                if is_adjacent_to_symbol(i, j, k - 1, grid):
                    sum_of_parts += int(number)

                # Skip the next characters that are part of this number
                j = k
            else:
                j += 1

    return sum_of_parts


def load_file():
    lines = []
    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines


# Example usage:
lines = load_file()


print(sum_part_numbers(lines))

def sum_adjacent_multiplications(data):
    total_sum = 0
    grid = [list(line) for line in data]

    # Function to find and return numbers adjacent to a given position
    def find_adjacent_numbers(x, y, grid, processed):
        adjacent_numbers = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the current cell
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny].isdigit():
                    if (nx, ny) in processed:
                        continue  # Skip if this digit is part of a number already processed

                    # Check to the left for the start of the number
                    start_y = ny
                    while start_y > 0 and grid[nx][start_y - 1].isdigit():
                        start_y -= 1

                    # Construct the full number
                    number = ''
                    while start_y < len(grid[0]) and grid[nx][start_y].isdigit():
                        number += grid[nx][start_y]
                        processed.add((nx, start_y))  # Mark this cell as processed
                        start_y += 1

                    adjacent_numbers.append(int(number))

        return adjacent_numbers

    # Iterate over each cell in the grid
    processed_digits = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '*':
                # Find numbers adjacent to the asterisk
                numbers = find_adjacent_numbers(i, j, grid, processed_digits)
                if len(numbers) == 2:
                    # Multiply the two numbers and add to the total sum
                    total_sum += numbers[0] * numbers[1]

    return total_sum

# Example usage:
# Assuming 'input_lines' contains the data from your file
print(sum_adjacent_multiplications(lines))