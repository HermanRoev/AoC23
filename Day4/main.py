def extract_matches(card_string):
    # Split the string at the '|'
    parts = card_string.split('|')

    # Extract numbers from each part
    numbers_before_pipe = [int(num) for num in parts[0].split() if num.isdigit()]
    numbers_after_pipe = [int(num) for num in parts[1].split() if num.isdigit()]

    matches = len(set(numbers_before_pipe) & set(numbers_after_pipe))

    return matches


def load_file(file_name):
    file = open(file_name, "r")
    cards_list = file.readlines()
    return cards_list

class Card:
    def __init__(self, card_id, matches):
        self.card_id = card_id
        self.matches = matches
        self.number_of_cards = 1  # Starts with 1 (the original card)

    def add_cards(self, additional_cards):
        # Update the number of cards based on matches
        self.number_of_cards += additional_cards

    def __repr__(self):
        return f"Card {self.card_id}: Matches = {self.matches}, Total Cards = {self.number_of_cards}"


def cards_list(cards):
    card_list = []
    id = 1
    for card in cards:
        card_list.append(Card(id, extract_matches(card)))
        id += 1
    return card_list


def calculate_cards_based_on_matches(cards):
    for i in range(len(cards)):
        matches = cards[i].matches
        for j in range(matches):
            cards[i + j + 1].add_cards(cards[i].number_of_cards)


def calculate_total_cards(cards):
    total_cards = 0
    for card in cards:
        total_cards += card.number_of_cards
    return total_cards


cards = cards_list(load_file("cards.txt"))
calculate_cards_based_on_matches(cards)
print(calculate_total_cards(cards))

