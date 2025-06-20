import random

GAME_RULES = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 20
OPERATORS = ['+', '-', '*']


def play():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, first_number)
    operator = random.choice(OPERATORS)

    math_expression = f"{first_number} {operator} {second_number}"
    correct_answer = str(eval(math_expression))

    return math_expression, correct_answer


if __name__ == "__main__":
    play()

