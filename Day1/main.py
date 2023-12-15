def extract_and_combine(filename):
    # Mapping of written digits to their numeric equivalents
    digit_mapping = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    def find_first_digit(s):
        temp_word = ''
        for char in s:
            if char.isdigit():
                return char
            elif char.isalpha():
                temp_word += char.lower()
                # Check if temp_word or any of its suffix is a valid digit word
                for i in range(len(temp_word)):
                    if temp_word[i:] in digit_mapping:
                        return digit_mapping[temp_word[i:]]
        return None

    def find_last_digit(s):
        temp_word = ''
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char.isdigit():
                return char
            elif char.isalpha():
                temp_word = char.lower() + temp_word
                # Check if temp_word or any of its prefix is a valid digit word
                for i in range(1, len(temp_word) + 1):
                    if temp_word[:i] in digit_mapping:
                        return digit_mapping[temp_word[:i]]
        return None

    total_sum = 0
    with open(filename, 'r') as file:
        for line in file:
            first_digit = find_first_digit(line)
            last_digit = find_last_digit(line)

            if first_digit and last_digit:
                combined_num = int(first_digit + last_digit)
                total_sum += combined_num

    return total_sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(extract_and_combine('input.txt'))

