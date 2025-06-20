import random

GAME_RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 20


def gcd(num1, num2):
    '''Naive gcd calculation'''
    gcd_result = 1

    for i in range(1, min(num1, num2) + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd_result = i

    return gcd_result


def play():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{first_number} {second_number}"
    correct_answer = str(gcd(first_number, second_number))

    return question, correct_answer