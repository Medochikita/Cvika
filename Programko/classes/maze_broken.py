"""
Escape the Maze

A simple game in which the user moves through a maze and tries to escape.
The user can move up, down, left, or right.

'P' represents the player,
'E' is the exit
'#' are walls
'O' are obstacles

The initial version of the code was generated by ChatGPT and then slightly modified.
"""

# Define the maze as a 2D grid
maze = [
    ['#', 'P', '#', 'E', '#'],
    ['#', ' ', 'O', ' ', '#'],
    ['#', ' ', 'O', ' ', '#'],
    ['#', ' ', 'O', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#']
]

# Player's initial position
player_x = 0
player_y = 1


def print_maze():
    """Prints the maze to the screen."""
    for row in maze:
        print(' '.join(row))


def move(direction):
    """Moves the player in the maze."""
    global player_x, player_y
    
    if direction == 'up':
        new_x = player_x - 1
        new_y = player_y
    elif direction == 'down':
        new_x = player_x + 1
        new_y = player_y
    elif direction == 'left':
        new_x = player_x
        new_y = player_y - 1
    elif direction == 'right':
        new_x = player_x
        new_y = player_y + 1
    else:
        print('wrong input')
        return
    
    if maze[new_x][new_y] != '#' and maze[new_x][new_y] != 'O':
        maze[player_x][player_y] = ' '  # Clear the current position
        player_x, player_y = new_x, new_y
        maze[player_x][player_y] = 'P'  # Set the new position
    else:
        print("You can't move there!")

# Main game loop
while True:
    print_maze()
    move_direction = input("Enter a direction (up, down, left, right): ")
    move(move_direction)
    
    if player_x == 0 and player_y == 3:
        print("Congratulations! You've reached the exit.")
        break
