# Needed to create random numbers to simulate dice roll
import random

# Initialise player scores to 0
player1_score = 0
player2_score = 0

# Repeat everything in this block 10 times
play_again=True
while play_again:

    # Generate random numbers between 1 and 6 for each player.
    input("player 1 press enter: ")
    player1_value = random.randint(1, 6)
    print(player1_value)
    input("player 2 press enter:")
    player2_value = random.randint(1, 6)
    print(player2_value)

    # Display the values
    print("Player 1 rolled: ", player1_value)
    print("Player 2 rolled: ", player2_value)

    # Selection: based on comparison of the values, take the appropriate path through the code.
    if player1_value > player2_value:
        print("player 1 wins.")
        player1_score = player1_score + 1  # This is how we increment a variable
    elif player2_value > player1_value:
        print("player 2 wins")
        player2_score = player2_score + 1
    else:
        print("It's a draw")

    d=input("Press Yes to continue or No to end:")  # Wait for user input to proceed.
    if d=="No":
        break
print("### Game Over ###")
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)