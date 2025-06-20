import random

GAME_RULES = "What number is missing in the progression?"

MIN_NUMBER = 1
MAX_NUMBER = 10


def play():
    start_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    step_of_progress = random.randint(MIN_NUMBER, MAX_NUMBER)
    length_of_progression = 10
    hidden_position = random.randint(0, length_of_progression - 1)

    progression = [start_number + step_of_progress * i for i in range(length_of_progression)]
    correct_answer = str(progression[hidden_position])
    progression[hidden_position] = '..'

    return ' '.join(map(str, progression)), correct_answer


if __name__ == "__main__":
    play()
