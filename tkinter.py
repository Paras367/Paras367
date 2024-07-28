import tkinter as tk
import random

# Initialize the game board
def init_board():
    return [[0] * 4 for _ in range(4)]

# Add a new tile (2 or 4) to the board at a random empty position
def add_tile(board):
    empty_positions = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_positions:
        return
    i, j = random.choice(empty_positions)
    board[i][j] = random.choice([2, 4])

# Check if the board has any possible moves left
def has_moves(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return True
            if i < 3 and board[i][j] == board[i + 1][j]:
                return True
            if j < 3 and board[i][j] == board[i][j + 1]:
                return True
    return False

# Move and merge the tiles in the given direction
def move(board, direction):
    def slide(row):
        new_row = [i for i in row if i != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [i for i in new_row if i != 0]
        return new_row + [0] * (4 - len(new_row))

    if direction == 'Left':
        board = [slide(row) for row in board]
    elif direction == 'Right':
        board = [slide(row[::-1])[::-1] for row in board]
    elif direction == 'Up':
        board = list(map(list, zip(*[slide(list(row)) for row in zip(*board)])))
    elif direction == 'Down':
        board = list(map(list, zip(*[slide(list(row[::-1]))[::-1] for row in zip(*board)])))
    return board

# Update the GUI board
def update_gui(board, labels):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            labels[i][j].config(text=str(value) if value != 0 else '', bg=get_color(value))

# Get color for a given tile value
def get_color(value):
    colors = {
        0: '#cdc1b4', 2: '#eee4da', 4: '#ede0c8', 8: '#f2b179', 16: '#f59563',
        32: '#f67c5f', 64: '#f65e3b', 128: '#edcf72', 256: '#edcc61', 512: '#edc850',
        1024: '#edc53f', 2048: '#edc22e'
    }
    return colors.get(value, '#cdc1b4')

# Handle user input
def key_press(event):
    global board
    direction = event.keysym
    if direction in ('Left', 'Right', 'Up', 'Down'):
        new_board = move(board, direction)
        if new_board != board:
            board = new_board
            add_tile(board)
            update_gui(board, labels)
            if not has_moves(board):
                game_over()

# Display game over message
def game_over():
    game_over_label = tk.Label(root, text="Game Over!", font=('Helvetica', 48), fg='red')
    game_over_label.place(relx=0.5, rely=0.5, anchor='center')

# Initialize the game
board = init_board()
add_tile(board)
add_tile(board)

# Set up the GUI
root = tk.Tk()
root.title("2048 Game")

frame = tk.Frame(root)
frame.grid()

labels = [[tk.Label(frame, text='', font=('Helvetica', 24), width=4, height=2, bg=get_color(0)) for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        labels[i][j].grid(row=i, column=j, padx=5, pady=5)

update_gui(board, labels)

root.bind('<Key>', key_press)
root.mainloop()
