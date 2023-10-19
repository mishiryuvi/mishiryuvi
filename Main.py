#Code for playing tic tac tao with coumpter

import tkinter as tk
import tkinter.messagebox
import random
import subprocess

# Check if the tkinter library is available, and if not, install it using apt-get
try:
    import tkinter
except ImportError:
    print("Tkinter is not available. Installing it...")
    subprocess.run(['sudo', 'apt-get', 'install', 'python3-tk', '-y'])

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all(all(cell != "" for cell in row) for row in board)

def on_click(row, col):
    if board[row][col] == "" and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(board, current_player):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif is_full(board):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game()
        else:
            switch_player()
            if current_player == "O" and not game_over:
                computer_move()

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global game_over, current_player
    game_over = False
    current_player = "X"
    for row in range(3):
        for col in range(3):
            board[row][col] = ""
            buttons[row][col].config(text="")
    label.config(text=f"Player {current_player}'s turn")

def computer_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = current_player
        buttons[r][c].config(text=current_player)
        if check_winner(board, current_player):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif is_full(board):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game()
        else:
            switch_player()

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
game_over = False
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None, None, None], [None, None, None], [None, None, None]]

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", width=10, height=2, command=lambda row=row, col=col: on_click(row, col))
        buttons[row][col].grid(row=row, column=col)

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Helvetica", 14))
label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
