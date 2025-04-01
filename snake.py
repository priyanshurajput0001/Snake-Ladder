import os
import time
import random

# ANSI escape codes for terminal colors
BOLD = "\033[1m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0m"  # Reset color

class SnakeLadderGame:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.positions = [0, 0]
        self.last_rolls = [0, 0]
        self.snakes = {96: 42, 94: 71, 75: 32, 47: 16, 37: 3, 28: 10}
        self.ladders = {4: 56, 12: 50, 14: 55, 22: 58, 41: 79, 54: 88}
    
    def clear_screen(self):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_board(self):
        print("Snakes: ", self.snakes)
        print("Ladders:", self.ladders)
        for i in range(100, 0, -1):
            if i % 10 == 0:
                print(f"\n{i:3}", end=" ")
            elif i in self.positions:
                # Highlight the player's name with color
                player_idx = self.positions.index(i)
                if self.players[player_idx] == "Computer":
                    print(f"{YELLOW}C{RESET}", end="")  # Display 'C' for computer
                else:
                    print(f"{CYAN}{self.players[player_idx][0]}{RESET}", end="")  # Display first letter of player name
            else:
                print(f"{i:3}", end=" ")
        print("\n", self.players[0], ":", self.positions[0], " | ", self.players[1], ":", self.positions[1])

    def roll_dice(self, player_idx):
        if self.players[player_idx] != "Computer":
            input(f"\n{YELLOW}{self.players[player_idx]}'s turn. Press Enter to roll... ")
            print(f"🎲 {BOLD}Rolling...")
            time.sleep(2)  # Simulate the rolling animation
        roll = random.randint(1, 6)
        print(f"{BOLD}{self.players[player_idx]} rolled a {roll}")
        return roll

    def move(self, player_idx):
        roll = self.roll_dice(player_idx)
        if self.positions[player_idx] == 0 and roll == 6:
            self.positions[player_idx] = 1
        elif self.positions[player_idx] + roll <= 100:
            self.positions[player_idx] += roll
        self.positions[player_idx] = self.snakes.get(self.positions[player_idx], self.positions[player_idx])
        self.positions[player_idx] = self.ladders.get(self.positions[player_idx], self.positions[player_idx])
        return roll

    def start_game(self):
        turn = 0
        while all(pos < 100 for pos in self.positions):
            self.clear_screen()
            self.print_board()
            print(f"{self.players[turn]}'s move:")
            self.move(turn)
            
            # Check for winner
            if self.positions[0] == 100:
                print(f"\n{BOLD}{YELLOW}{self.players[0]} is the Winner! 🏆{RESET}")
                break
            elif self.positions[1] == 100:
                print(f"\n{BOLD}{CYAN}{self.players[1]} is the Winner! 🏆{RESET}")
                break
            
            turn = 1 - turn  # Toggle between player 1 and player 2

# Main Menu
print("\n🎲 WELCOME TO SNAKE & LADDER GAME 🎲")
print("1. Player vs Player")
print("2. Player vs Computer")
print("3. Exit")

choice = int(input("Enter choice: "))
if choice in [1, 2]:
    player1 = input("Enter Player 1 Name: ")
    player2 = "Computer" if choice == 2 else input("Enter Player 2 Name: ")
    game = SnakeLadderGame(player1, player2)
    game.start_game()
