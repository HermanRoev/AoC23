from itertools import count


def load_data(file_path):
    with open(file_path, 'r') as file:
        # Read the entire file and split it into sections based on blank lines
        sections = file.read().strip().split('\n\n')

    # For each section, split it into lines and save these lines in a list
    all_sections = [section.split('\n') for section in sections]

    return all_sections


#Task 1
def horizontal_mirror(pattern):
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:  # Check if two adjacent lines are the same
            j = 1
            while i - j >= 0 and i + 1 + j < len(pattern):
                if pattern[i - j] != pattern[i + 1 + j]:
                    break  # Break if the mirroring condition fails
                j += 1
            else:
                # Add the starting indices of the mirrored section
                return i+1
    return 0


def vertical_mirror(pattern):
    num_rows = len(pattern)
    num_columns = len(pattern[0])

    for col in range(num_columns - 1):  # Iterate through each column
        # Check if two adjacent columns are the same
        if all(pattern[row][col] == pattern[row][col + 1] for row in range(num_rows)):
            offset = 1
            while col - offset >= 0 and col + 1 + offset < num_columns:
                if not all(pattern[row][col - offset] == pattern[row][col + 1 + offset] for row in range(num_rows)):
                    break  # Break if the mirroring condition fails
                offset += 1
            else:
                # Add the starting indices of the mirrored section (col, col + 1)
                return col+1
    return 0


def count_mismatches(line1, line2):
    mismatches = 0
    for c1, c2 in zip(line1, line2):
        if c1 != c2:
            mismatches += 1
    return mismatches


def horizontal_mirror_with_one_error(pattern):
    num_lines = len(pattern)

    for line in range(num_lines - 1):
        # Check for potential mirrored pair of lines
        if count_mismatches(pattern[line], pattern[line + 1]) <= 1:
            total_errors = count_mismatches(pattern[line], pattern[line + 1])
            offset = 1

            while line - offset >= 0 and line + 1 + offset < num_lines and total_errors <= 1:
                # Check for mirroring extending outward
                total_errors += count_mismatches(pattern[line - offset], pattern[line + 1 + offset])
                offset += 1

            if total_errors == 1:  # Exactly one error in the entire mirrored section
                return line + 1
    return 0


def vertical_mirror_with_one_error(pattern):
    transposed_pattern = [''.join(pattern[row][col] for row in range(len(pattern))) for col in range(len(pattern[0]))]
    return horizontal_mirror_with_one_error(transposed_pattern)


# Load the data using the function
loaded_data = load_data('input.txt')
horizontal_sections = []
vertical_sections = []
sum = 0

for pattern in loaded_data:
    horizontal_sections.append(horizontal_mirror(pattern))
    vertical_sections.append(vertical_mirror(pattern))

for number in horizontal_sections:
    sum += (number * 100)

for number in vertical_sections:
    sum += number

print(sum)

sum = 0
horizontal_sections = []
vertical_sections = []

for pattern in loaded_data:
    horizontal_sections.append(horizontal_mirror_with_one_error(pattern))
    vertical_sections.append(vertical_mirror_with_one_error(pattern))

for number in horizontal_sections:
    sum += (number * 100)

for number in vertical_sections:
    sum += number

print(sum)