class GameGUI:
    def __init__(self):
        # Initialize game attributes, such as the game board and player's position
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.player_x = 0
        self.player_y = 0
        self.trap_positions = [(2, 2), (4, 5)]  # Example trap positions
        self.prize_positions = [(1, 3), (3, 6)]  # Example prize positions
        self.steps = 0

    def createBoard(self):
        # Initialize the game board with walls, traps, and prizes
        pass  # Implement board creation logic here

    def replay(self):
        # Implement the replay functionality
        pass

    def pickupPrize(self):
        # Implement prize pickup logic
        pass

    def isTrap(self, px, py):
        # Check if the player is on a trap
        return (self.player_x, self.player_y) in self.trap_positions

    def springTrap(self, px, py):
        # Implement the trap springing logic
        pass

    def movePlayer(self, px, py):
        # Move the player and update the game board
        self.player_x += px
        self.player_y += py
        self.steps += 1
        pass  # Implement player movement logic

    def endGame(self):
        # Check if the game has ended (e.g., player reached the end) and return the final score
        pass

    def getSteps(self):
        return self.steps

# You'll need to implement the methods in the GameGUI class with your game's logic and rules.


def main():
    game = GameGUI()
    game.createBoard()

    px, py = 0, 0
    score = 0

    valid_commands = ["right", "left", "up", "down", "jump", "pickup", "quit", "replay", "help"]

    print("Welcome to EscapeRoom!")
    print("Get to the other side of the room, avoiding walls and invisible traps.")
    print("Pick up all the prizes.\n")

    play = True
    while play:
        user_input = input("Enter a command: ").lower()

        if user_input == "quit":
            play = False
        elif user_input == "replay":
            score += game.replay()
            print("Score: " + str(score))
            print("Steps: " + str(game.getSteps()))
            print("Score has been reset.")
            score = 0
        elif user_input == "help":
            print("Valid commands: " + ", ".join(valid_commands))
        elif user_input == "pickup":
            score += game.pickupPrize()
        elif user_input == "right":
            px += 1
        elif user_input == "left":
            px -= 1
        elif user_input == "up":
            py -= 1
        elif user_input == "down":
            py += 1
        elif user_input == "jump":
            # Implement jumping logic here
            pass  # Placeholder for jumping logic

        # Check for traps and handle trap logic here
        if game.isTrap(px, py):
            score += game.springTrap(px, py)

        # Move the player and update the score
        score += game.movePlayer(px, py)

    # End the game and display final score and steps
    score += game.endGame()
    print("Final Score: " + str(score))
    print("Total Steps: " + str(game.getSteps()))

if __name__ == "__main__":
    main()