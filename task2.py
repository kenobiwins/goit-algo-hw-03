import random

MIN = 1
MAX = 1000

def get_numbers_ticket(min: int = MIN, max: int = MAX, quantity: int = 6) -> list:
    is_min_valid = MIN <= min
    is_max_valid = min <= max <= MAX
    is_quantity_valid = MIN <= quantity <= (max - min + 1)
    
    if not (is_min_valid and is_max_valid and is_quantity_valid):
        return list()

    winning_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(winning_numbers)
