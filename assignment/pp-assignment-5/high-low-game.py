import random

def high_low_game():
    score = 0
    rounds = 5

    for round_num in range(1, rounds + 1):
        # Generate a random number for the player and the computer
        # random.randint(1, 100)
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Round {round_num}")
        print(f"Your number is {player_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (higher h /lower l): ").strip().lower()

        if ((guess== 'h' or guess == 'higher') and player_number > computer_number) or ((guess == 'l' or guess == 'lower') and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")

    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    high_low_game()


