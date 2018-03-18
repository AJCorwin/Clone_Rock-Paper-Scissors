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
    running = "yes"
    player_name = player_name

    # While the player wants to continue the game will run
    while True:

        # this selects the random AI choice
        ai_picks = ['rock', 'paper', 'scissors']
        ai1_choice = random.choice(ai_picks)

        # if the player decides to stop the game will quit and print out the final score
        if running == "no":
            print("\nGoodbye", player_name, "The final score was\n"
                                            "Player 1:", p1_score, "Player 2:", p2_score)
            break

        elif running == "yes":
            player_choice = input("\nPlease pick rock, paper, or scissors ")

            if player_choice.lower() == "rock":
                running = "yes"
                if ai1_choice == "paper":
                    print("\nYou picked", player_choice, ",the AI picked", ai1_choice)

                    p2_score = p2_score + 1
                    print("\nYou lost this round,", player_name,
                          "\n Your score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()

                elif ai1_choice == "scissors":
                    print("\nYou picked", player_choice, ",the AI Picked", ai1_choice)
                    p1_score = p1_score + 1
                    print("\nYou won this round,", player_name,
                          "\n Your score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()
                    print(running)

                elif ai1_choice == "rock":
                    print("\nYou picked", player_choice, ",the AI Picked", ai1_choice)
                    print("\nThis round was a tie!,", player_name,
                          "\n Player 1's score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()

            elif player_choice.lower() == "paper":
                running = "yes"
                if ai1_choice == "scissors":
                    print("\nYou picked", player_choice, ",the AI picked", ai1_choice)

                    p2_score = p2_score + 1
                    print("\nYou lost this round,", player_name,
                          "\n Your score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()

                elif ai1_choice == "rock":
                    print("\nYou picked", player_choice, ",the AI Picked", ai1_choice)
                    p1_score = p1_score + 1
                    print("\nYou won this round,", player_name,
                          "\n Your score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()
                    print(running)

                elif ai1_choice == "paper":
                    print("\nYou picked", player_choice, ",the AI Picked", ai1_choice)
                    print("\nThis round was a tie!,", player_name,
                          "\n Player 1's score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()

            elif player_choice.lower() == "scissors":
                running = "yes"
                if ai1_choice == "rock":
                    print("\nYou picked", player_choice, ",the AI picked", ai1_choice)

                    p2_score = p2_score + 1
                    print("\nYou lost this round,", player_name,
                          "\n Your score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()

                elif ai1_choice == "paper":
                    print("\nYou picked", player_choice, ",the AI Picked", ai1_choice)
                    p1_score = p1_score + 1
                    print("\nYou won this round,", player_name,
                          "\n Your score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()
                    print(running)

                elif ai1_choice == "scissors":
                    print("\nYou picked", player_choice, ",the AI Picked", ai1_choice)
                    print("\nThis round was a tie!,", player_name,
                          "\n Player 1's score is", p1_score, ",Player 2's Score is", p2_score)

                    running = input("\nDo you want to play again?, Yes or No. ")
                    running = running.lower()


# AI vs AI game logic portion
def ai_vs_ai_game_logic():
    gamenum = 0
    ai1_score = 0
    ai2_score = 0
    rounds_to_run = input("\n\nHow many games would you like to simulate? numbers only please")
    rounds_to_run = int(rounds_to_run)


    while True:
        if gamenum < rounds_to_run:
            ai_picks = ['rock', 'paper', 'scissors']
            ai1_choice = random.choice(ai_picks)
            ai2_choice = random.choice(ai_picks)

            if ai1_choice.lower() == "rock":
                if ai2_choice == "paper":
                    print("\nAI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)

                    ai2_score = ai2_score + 1
                    print("\nAI 1 lost this round,",
                        "\n AI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

                elif ai2_choice == "scissors":
                    print("\nAI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)
                    ai1_score = ai1_score + 1
                    print("\nAI 1 won this round,",
                         "\n AI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

                elif ai2_choice == "rock":
                    print("\nThis round was a tie. AI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)
                    print("\nAI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

            elif ai1_choice.lower() == "paper":
                if ai2_choice == "rock":
                    print("\nAI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)

                    ai1_score = ai1_score + 1
                    print("\nAI 2 lost this round,",
                        "\n AI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

                elif ai2_choice == "scissors":
                    print("\nAI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)
                    ai2_score = ai2_score + 1
                    print("\nAI 2 won this round,",
                        "\n AI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

                elif ai2_choice == "paper":
                    print("\nAI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)
                    print("\nAI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

            elif ai1_choice.lower() == "scissors":
                if ai2_choice == "paper":
                    print("\nAI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)

                    ai1_score = ai1_score + 1
                    print("\nAI 1 lost this round,",
                        "\n AI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

                elif ai2_choice == "rock":
                    print("\nAI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)
                    ai2_score = ai2_score + 1
                    print("\nAI 2 won this round,",
                            "\n AI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

                elif ai2_choice == "scissors":
                    print("\nAI 1 picked", ai1_choice, ",AI 2 picked", ai2_choice)
                    print("\nAI 1's score is ", ai1_score, ",AI 2's score is", ai2_score)

                    gamenum = gamenum + 1

        elif gamenum == rounds_to_run:
            print("\n\nThe final score was:\n"
                  "AI 1's score is", ai1_score, ", AI 2's score is", ai2_score)
            break
game()
