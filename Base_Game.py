import random


# todo: implement AI vs AI
# todo: improve game logic

def game():
    # Starts the game, essentially a basic splash screen
    player_name = input("What is your name player? \n")
    print("Hello", player_name)

    player_playing = input("Do you want to play?\nYes or No\n")
    if player_playing.lower() == "play":
        print("You are player 1\n")
        number_of_ai = 1
        gamelogic(number_of_ai, player_name)

    if player_playing.lower() == "yes":
        print("You are player 1\n")
        number_of_ai = 1
        gamelogic(number_of_ai, player_name)

    elif player_playing.lower() == "no":
        ai_playing = input("Do you want the AI to play against itself?\nYes or No\n")
        if ai_playing.lower() == "yes":
            number_of_ai = 2
            gamelogic(number_of_ai, player_name)
        else:
            print("Goodbye for now")
    else:
        print("\nThat is not an acceptable answer, goodbye")


# Game logic portion of Rock Paper Scissors
def gamelogic(number_of_ai, player_name):
    p1_score = 0
    p2_score = 0
    running = "yes"
    ai_players = number_of_ai
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


game()
