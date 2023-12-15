def count_arrangements_simple(line):
    """
    Simplified function to count the number of valid arrangements for a given line of spring conditions and group sizes.
    """
    parts = line.split()
    conditions = parts[0]  # Condition of each spring
    group_sizes = list(map(int, parts[1].split(',')))  # Sizes of groups of damaged springs

    def generate_combinations(conditions):
        """
        Generate all possible combinations by replacing '?' with either '.' or '#'.
        """
        if '?' not in conditions:
            return [conditions]

        index = conditions.index('?')
        # Replace '?' with operational spring
        with_dot = conditions[:index] + '.' + conditions[index + 1:]
        # Replace '?' with damaged spring
        with_hash = conditions[:index] + '#' + conditions[index + 1:]

        return generate_combinations(with_dot) + generate_combinations(with_hash)

    def is_valid_combination(combination):
        """
        Check if a given combination of springs meets the criteria.
        """
        group_counts = []
        count = 0
        for spring in combination:
            if spring == '#':
                count += 1
            elif count > 0:
                group_counts.append(count)
                count = 0
        if count > 0:
            group_counts.append(count)

        return group_counts == group_sizes

    valid_combinations = 0
    for combo in generate_combinations(conditions):
        if is_valid_combination(combo):
            valid_combinations += 1

    return valid_combinations


with open('input.txt') as f:
    data = f.readlines()

# Test the simplified function with the provided example data
#total_arrangements_simple = sum(count_arrangements_simple(line) for line in data)
#print(total_arrangements_simple)