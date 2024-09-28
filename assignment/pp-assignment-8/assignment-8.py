class BucketPuzzleGame:
    def __init__(self):
        self.B3 = 0  # 3-liter bucket
        self.B5 = 0  # 5-liter bucket
        self.B8 = 8  # 8-liter bucket (starts full)
    
    def display(self):
        """Displays the current state of all buckets."""
        print(f"\n8| {'W' * self.B8}{' ' * (8 - self.B8)} |")
        print(f"7|         |")
        print(f"6|         |")
        print(f"5|         |       5|{'W' * self.B5}{' ' * (5 - self.B5)} |")
        print(f"4|         |        4|         |")
        print(f"3|         |        3|         |        3| {'W' * self.B3}{' ' * (3 - self.B3)} |")
        print(f"2|         |        2|         |        2|         |")
        print(f"1|         |        1|         |        1|         |")
        print(" +----------+         +----------+         +------+\n")
        print(f"   8L                   5L                  3L\n")


    def fill(self, bucket):
        """Fill a specific bucket."""
        if bucket == '8':
            self.B8 = 8
        elif bucket == '5':
            self.B5 = 5
        elif bucket == '3':
            self.B3 = 3
    
    def empty(self, bucket):
        """Empty a specific bucket."""
        if bucket == '8':
            self.B8 = 0
        elif bucket == '5':
            self.B5 = 0
        elif bucket == '3':
            self.B3 = 0
    
    def pour(self, from_bucket, to_bucket):
        """Pour water from one bucket into another."""
        if from_bucket == '8' and to_bucket == '5':
            transfer_amount = min(self.B8, 5 - self.B5)
            self.B8 -= transfer_amount
            self.B5 += transfer_amount
        elif from_bucket == '8' and to_bucket == '3':
            transfer_amount = min(self.B8, 3 - self.B3)
            self.B8 -= transfer_amount
            self.B3 += transfer_amount
        elif from_bucket == '5' and to_bucket == '8':
            transfer_amount = min(self.B5, 8 - self.B8)
            self.B5 -= transfer_amount
            self.B8 += transfer_amount
        elif from_bucket == '5' and to_bucket == '3':
            transfer_amount = min(self.B5, 3 - self.B3)
            self.B5 -= transfer_amount
            self.B3 += transfer_amount
        elif from_bucket == '3' and to_bucket == '8':
            transfer_amount = min(self.B3, 8 - self.B8)
            self.B3 -= transfer_amount
            self.B8 += transfer_amount
        elif from_bucket == '3' and to_bucket == '5':
            transfer_amount = min(self.B3, 5 - self.B5)
            self.B3 -= transfer_amount
            self.B5 += transfer_amount

    def check_win(self):
        """Check if any bucket contains exactly 4 liters of water."""
        return self.B8 == 4 or self.B5 == 4 or self.B3 == 4

    def play(self):
        """Main loop to play the puzzle game."""
        print("Welcome to the Bucket Puzzle!")
        while True:
            self.display()
            
            if self.check_win():
                print("Congratulations! You got exactly 4 liters of water in one of the buckets.")
                break
            
            command = input("Select a bucket 8, 5, 3, or (q)QUIT: ").lower()

            if command == '8' or command == '5' or command == '3':
                action = input(f"(F)ill, (E)mpty, or (P)our from bucket {command}? ").lower()
                
                if action == 'f':
                    self.fill(command)
                elif action == 'e':
                    self.empty(command)
                elif action == 'p':
                    to_bucket = input("Which bucket would you like to pour into? (8, 5, 3): ").strip()
                    if to_bucket != command and to_bucket in ['8', '5', '3']:
                        self.pour(command, to_bucket)
                    else:
                        print("Invalid pour operation.")
                else:
                    print("Invalid action.")
            elif command == 'quit' or command == 'q':
                print("Quitting the game. Goodbye!")
                break
            else:
                print("Invalid command, please try again.")

# Create a game instance and start playing
game = BucketPuzzleGame()
game.play()
