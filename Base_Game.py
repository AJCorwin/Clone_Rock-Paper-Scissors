import random

#todo: implement AI vs AI
#todo: change all variable names to lowercase
#todo: improve game logic

def Game():

    ##Starts the game, essentially a basic splash screen
    PlayerName = input("What is your name player? \n")
    print("Hello",PlayerName)

    PlayerPlaying = input("Do you want to play?\nYes or No\n")
    if PlayerPlaying.lower() == "play":
        print("You are player 1\n")
        NumberOfAi = 1
        GameLogic(NumberOfAi,PlayerName)

    if PlayerPlaying.lower() == "yes":
        print("You are player 1\n")
        NumberOfAi = 1
        GameLogic(NumberOfAi,PlayerName)

    elif PlayerPlaying.lower() == "no":
        NumberOfAi = 2
        GameLogic(NumberOfAi,PlayerName)

    else: print("\nThat is not an acceptable answer, goodbye")

#Game logic portion of Rock Paper Scissors
def GameLogic(NumberOfAi,PlayerName):

    P1_Score = 0
    P2_Score = 0
    Running = "yes"
    AIPlayers = NumberOfAi
    PlayerName = PlayerName

    #While the player wants to continue the game will run
    while True:

        #this selects the random AI choice
        AIPicks = ['rock', 'paper', 'scissors']
        AI1_Choice = random.choice(AIPicks)

        #if the player decides to stop the game will quit and print out the final score
        if Running == "no":
            print("\nGoodbye", PlayerName,"The final score was\n"
                  "Player 1:", P1_Score, "Player 2:", P2_Score)
            break

        elif Running == "yes":
            Player_Choice = input("\nPlease pick rock, paper, or scissors ")

            if Player_Choice.lower() == "rock":
                Running = "yes"
                if AI1_Choice == "paper":
                    print("\nYou picked", Player_Choice, ",the AI picked", AI1_Choice)

                    P2_Score = P2_Score + 1
                    print("\nYou lost this round,",PlayerName,
                        "\n Your score is", P1_Score, ",Player 2's Score is",P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()

                elif AI1_Choice == "scissors":
                    print("\nYou picked",Player_Choice,",the AI Picked",AI1_Choice)
                    P1_Score = P1_Score + 1
                    print("\nYou won this round,", PlayerName,
                        "\n Your score is", P1_Score, ",Player 2's Score is", P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()
                    print(Running)

                elif AI1_Choice == "rock":
                    print("\nYou picked",Player_Choice,",the AI Picked",AI1_Choice)
                    print("\nThis round was a tie!,", PlayerName,
                    "\n Player 1's score is", P1_Score, ",Player 2's Score is", P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()

            elif Player_Choice.lower() == "paper":
                Running = "yes"
                if AI1_Choice == "scissors":
                    print("\nYou picked", Player_Choice, ",the AI picked", AI1_Choice)

                    P2_Score = P2_Score + 1
                    print("\nYou lost this round,",PlayerName,
                        "\n Your score is", P1_Score, ",Player 2's Score is",P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()

                elif AI1_Choice == "rock":
                    print("\nYou picked",Player_Choice,",the AI Picked",AI1_Choice)
                    P1_Score = P1_Score + 1
                    print("\nYou won this round,", PlayerName,
                        "\n Your score is", P1_Score, ",Player 2's Score is", P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()
                    print(Running)

                elif AI1_Choice == "paper":
                    print("\nYou picked",Player_Choice,",the AI Picked",AI1_Choice)
                    print("\nThis round was a tie!,", PlayerName,
                    "\n Player 1's score is", P1_Score, ",Player 2's Score is", P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()

            elif Player_Choice.lower() == "scissors":
                Running = "yes"
                if AI1_Choice == "rock":
                    print("\nYou picked", Player_Choice, ",the AI picked", AI1_Choice)

                    P2_Score = P2_Score + 1
                    print("\nYou lost this round,",PlayerName,
                        "\n Your score is", P1_Score, ",Player 2's Score is",P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()

                elif AI1_Choice == "paper":
                    print("\nYou picked",Player_Choice,",the AI Picked",AI1_Choice)
                    P1_Score = P1_Score + 1
                    print("\nYou won this round,", PlayerName,
                        "\n Your score is", P1_Score, ",Player 2's Score is", P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()
                    print(Running)

                elif AI1_Choice == "scissors":
                    print("\nYou picked",Player_Choice,",the AI Picked",AI1_Choice)
                    print("\nThis round was a tie!,", PlayerName,
                    "\n Player 1's score is", P1_Score, ",Player 2's Score is", P2_Score)

                    Running = input("\nDo you want to play again?, Yes or No. ")
                    Running = Running.lower()

Game()



