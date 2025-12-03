import tkinter as tk
from tkinter import messagebox
import random

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Score variables
player_score = 0
computer_score = 0

# Functions
def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = f"Tie! Both chose {player_choice}"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = f"You Win! {player_choice} beats {computer_choice}"
        player_score += 1
    else:
        result = f"You Lose! {computer_choice} beats {player_choice}"
        computer_score += 1

    # Update result label
    result_label.config(text=result)
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

# Widgets
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20)).pack(pady=10)
tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Player: 0  Computer: 0", font=("Arial", 14))
score_label.pack(pady=10)

# Exit button
tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

# Run the GUI
root.mainloop()
