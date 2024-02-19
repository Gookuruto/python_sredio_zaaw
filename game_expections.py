import threading
import time
from dataclasses import dataclass

# Define custom exceptions
class GameOverError(Exception):
    pass

class InvalidMoveError(Exception):
    pass

# Dataclass for representing player
@dataclass
class Player:
    name: str
    position: tuple

# Dataclass for representing the maze
@dataclass
class Maze:
    rows: int
    columns: int

    def is_valid_position(self, position):
        return 0 <= position[0] < self.rows and 0 <= position[1] < self.columns

# Decorator for logging player actions
def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{args[0].name} {func.__name__}")
        return result
    return wrapper

# Function to move the player within the maze
@log_action
def move_player(player, direction):
    row, col = player.position
    if direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1

    new_position = (row, col)
    if not maze.is_valid_position(new_position):
        raise InvalidMoveError("Invalid move!")

    player.position = new_position

# Function to run the game loop
def game_loop(player):
    while True:
        try:
            direction = input("Enter direction (up/down/left/right): ").lower()
            move_player(player, direction)
            print("Player moved successfully.")
            time.sleep(1)  # Simulate some processing time
        except InvalidMoveError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nGame paused.")
            choice = input("Do you want to continue playing? (yes/no): ").lower()
            if choice != 'yes':
                raise GameOverError("Game over.")
            else:
                print("Resuming game...")

if __name__ == "__main__":
    maze = Maze(rows=5, columns=5)
    player = Player(name="Player", position=(0, 0))

    try:
        game_thread = threading.Thread(target=game_loop, args=(player,))
        game_thread.start()
        game_thread.join()
    except GameOverError as e:
        print(e)
