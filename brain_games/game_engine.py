from brain_games.cli import welcome_user

GAME_ROUNDS = 3


def run(game_module):
    player_name = welcome_user()
    print(game_module.GAME_RULES)

    for _ in range(GAME_ROUNDS):
        question, correct_answer = game_module.play()

        print('Question: {}'.format(question))
        player_answer = input('Your answer: ')

        is_correct = player_answer == correct_answer

        if not is_correct:
            print(
                f"'{player_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'\n"
                f"Let's try again, {player_name}!"
            )
            return
        print('Correct!')

    print(f"Congratulations, {player_name}!")