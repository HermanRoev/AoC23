def parse_hand(hand):
    """Converts a hand into numerical values while preserving the original order."""
    card_values = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    return [card_values[card] if card in card_values else int(card) for card in hand]


def hand_type(hand):
    """Determines the type of a poker hand with joker rule."""
    counts = {card: hand.count(card) for card in set(hand)}
    joker_count = counts.pop(1, 0)  # Remove Jokers and get their count

    if joker_count == 5:
        return 7 # five_of_a_kind

    if joker_count > 0:
        # Add joker count to the highest count of other cards
        max_count_card = max(counts, key=counts.get)
        counts[max_count_card] += joker_count

    if len(counts) == 1:
        return 7  # five_of_a_kind
    if 4 in counts.values():
        return 6  # four_of_a_kind
    if sorted(counts.values()) == [2, 3]:
        return 5  # full_house
    if 3 in counts.values():
        return 4  # three_of_a_kind
    if len(counts) == 3:
        return 3  # two_pair
    if 2 in counts.values():
        return 2  # one_pair
    return 1  # high_card


# Modification in sort_hands function
def sort_hands(hands):
    parsed_hands = [(hand, parse_hand(hand), bid) for hand, bid in hands]
    hands_with_types = [(hand, bid, hand_type(parsed_hand), parsed_hand) for hand, parsed_hand, bid in parsed_hands]
    return sorted(hands_with_types, key=lambda x: (x[2], x[3]))


def calculate_winnings(input_hands):
    """Calculates total winnings based on hand ranks and bids."""
    hands = [line.split() for line in input_hands]
    hands = [(hand[0], int(hand[1])) for hand in hands]
    sorted_hands = sort_hands(hands)
    total_winnings = sum(bid * (rank + 1) for rank, (hand, bid, _, _) in enumerate(sorted_hands))
    return total_winnings


input_hands = []
with open("input.txt") as f:
    input = f.readlines()
    for line in input:
        input_hands.append(line.strip())


total_winnings = calculate_winnings(input_hands)
print(f"Total winnings: {total_winnings}")
