import random


# todo: improve game logic
# todo: Clean up sentence syntax.


def game():
    # Starts the game, essentially a basic splash screen
    player_name = input("What is your name player? \n")
    print("Hello", player_name)

    player_playing = input("Do you want to play?\nYes or No\n")
    if player_playing.lower() == "play":
        print("You are player 1\n")
        player_vs_ai_game_logic(player_name)

    if player_playing.lower() == "yes":
        print("You are player 1\n")
        player_vs_ai_game_logic(player_name)

    elif player_playing.lower() == "no":
        ai_playing = input("Do you want the AI to play against itself?\nYes or No\n")
        if ai_playing.lower() == "yes":
            ai_vs_ai_game_logic()
        else:
            print("\nGoodbye for now")
    else:
        print("\nThat is not an acceptable answer, goodbye")


# Player vs AI game logic portion
def player_vs_ai_game_logic(player_name):
    p1_score = 0
    p2_score = 0
    numofties = 0

    running = "yes"
    player_name = player_name

    check_dict = {'rock:rock': 'Tied', 'paper:paper': 'Tied', 'scissors:scissors': 'Tied',
                  'rock:scissors': 'Won', 'scissors:paper': 'Won', 'paper:rock': 'Won',
                  'rock:paper': 'Lost', 'scissors:rock': 'Lost', 'paper:scissors': 'Lost'}

    # While the player wants to continue the game will run
    while True:
        # this selects the random AI choice
        ai_picks = ['rock', 'paper', 'scissors']
        choice_2 = random.choice(ai_picks)

        # if the player decides to stop the game will quit and print out the final score
        if running == "no":
            print("\nGoodbye", player_name, "The final score was\n"
                                            "Player 1:", p1_score, "Player 2:", p2_score)
            break

        elif running == "yes":
            choice_1 = input("\nPlease pick rock, paper, or scissors ").lower()
            combined_choice = choice_1 + ":" + choice_2

            if check_dict.get(combined_choice) == "Won":
                p1_score = p1_score + 1
                print('Player 1 won this round, the current score is, Player 1: '
                      , p1_score, 'Player 2:', p2_score, 'Ties:', numofties)
                run_checker()

            elif check_dict.get(combined_choice) == "Lost":
                p2_score = p2_score + 1
                print('Player 2 won this round, the current score is, Player 1: '
                      , p1_score, 'Player 2:', p2_score, 'Ties:', numofties)
                run_checker()

            elif check_dict.get(combined_choice) == "Tied":
                numofties = numofties + 1
                print('No one won this round, the current score is, Player 1: '
                      , p1_score, 'Player 2:', p2_score, 'Ties:', numofties)
                run_checker()


# AI vs AI game logic portion
def ai_vs_ai_game_logic():
    gamenum = 0
    p1_score = 0
    p2_score = 0
    numofties = 0
    rounds_to_run = input("\n\nHow many games would you like to simulate? numbers only please\n")
    rounds_to_run = int(rounds_to_run)

    check_dict = {'rock:rock': 'Tied', 'paper:paper': 'Tied', 'scissors:scissors': 'Tied',
                  'rock:scissors': 'Won', 'scissors:paper': 'Won', 'paper:rock': 'Won',
                  'rock:paper': 'Lost', 'scissors:rock': 'Lost', 'paper:scissors': 'Lost'}

    while True:
        if gamenum < rounds_to_run:
            ai_picks = ['rock', 'paper', 'scissors']
            choice_1 = random.choice(ai_picks)
            choice_2 = random.choice(ai_picks)
            combined_choice = choice_1 + ":" + choice_2

            if check_dict.get(combined_choice) == "Won":
                p1_score = p1_score + 1
                print('Player 1 won this round, the current score is, Player 1: ',
                      p1_score, 'Player 2:', p2_score, 'Ties:', numofties)
                gamenum = gamenum + 1

            elif check_dict.get(combined_choice) == "Lost":
                p2_score = p2_score + 1
                print('Player 2 won this round, the current score is, Player 1: ',
                      p1_score, 'Player 2:', p2_score, 'Ties:', numofties)
                gamenum = gamenum + 1

            if check_dict.get(combined_choice) == "Tied":
                numofties = numofties + 1
                print('No one won this round, the current score is, Player 1: ',
                      p1_score, 'Player 2:', p2_score, 'Ties:', numofties)
                gamenum = gamenum + 1

        elif gamenum == rounds_to_run:
            print("\n\nThe final score was:\n"
                  "AI 1's score is", p1_score, ", AI 2's score is", p2_score, "total ties are:", numofties)
            break


def run_checker():
    running = input("\nDo you want to play again?, Yes or No. ")
    running = running.lower()
    return running


game()
