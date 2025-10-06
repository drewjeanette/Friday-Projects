import random

print("Welcome to Rock, Paper, Scissors!")
print("Type rock, paper, or scissors.")

playGame = True
 

while playGame:
    # Get the player's choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Generate the computer's choice (1–3)
    r_num = random.randint(1, 3)
    if r_num == 1:
        comp_choice = "rock"
    elif r_num == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"

    # Display choices
    print("You chose ", user_choice,". Computer chose ",comp_choice,".")

    # Determine the winner
    if user_choice == comp_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "scissors" and comp_choice == "paper") or
        (user_choice == "paper" and comp_choice == "rock")
    ):
        if user_choice == "rock" and comp_choice == "scissors":
            print("You win! Rock smashes scissors.")
        elif user_choice == "scissors" and comp_choice == "paper":
            print("You win! Scissors cut paper.")
        else:
            print("You win! Paper covers rock.")
    else:
        if comp_choice == "rock" and user_choice == "scissors":
            print("You lose! Rock smashes scissors.")
        elif comp_choice == "scissors" and user_choice == "paper":
            print("You lose! Scissors cut paper.")
        else:
            print("You lose! Paper covers rock.")

    # Ask to play again
    playGame = input("Do you want to play again? (yes/no): ").lower()
    if (playGame == "no"):
        print("Thanks for playing. Goodbye!")
        break
