import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def play():
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'

    return random_number, correct_answer


if __name__ == "__main__":
    play()
