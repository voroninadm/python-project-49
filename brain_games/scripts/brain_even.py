import random

import prompt

from brain_games.cli import welcome_user


def is_even():
    random_number = random.randint(1, 100)
    print(f"Question: {random_number}")
    user_answer = prompt.string('Your answer: ')

    correct_answer = 'yes' if random_number % 2 == 0 else 'no'

    if user_answer.lower() == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False


def main():
    player_name = welcome_user()
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(game_rules)

    total_games_count = 3
    current_game_score = 0

    while current_game_score < total_games_count:
        if is_even():
            current_game_score += 1
        else:
            print(f"Let's try again, {player_name}!")
            return

    print(f"Congratulations, {player_name}!")

    if __name__ == "__main__":
        main()
