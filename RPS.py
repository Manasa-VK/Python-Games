# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:03:41 2023

@author: karun
"""
import random
import tkinter as tk

# Initialize player and computer scores
player_score = 0
computer_score = 0

# Define a function to choose the computer's move
def computer_move():
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)

# Define a function to determine the winner of the game
def determine_winner(player_move, computer_move):
    global player_score, computer_score
    if player_move == 'rock' and computer_move == 'scissors':
        player_score += 2
        return 'Player'
    elif player_move == 'paper' and computer_move == 'rock':
        player_score += 2
        return 'Player'
    elif player_move == 'scissors' and computer_move == 'paper':
        player_score += 2
        return 'Player'
    elif player_move == computer_move:
        return 'Tie'
    else:
        computer_score += 1
        return 'Computer'

# Define a function to handle the player's move
def play(move):
    global player_score, computer_score
    computer = computer_move()
    result = determine_winner(move, computer)
    outcome_label.config(text='You chose {}, computer chose {}. {}. Player: {}, Computer: {}'.format(move, computer, result, player_score, computer_score))

# Set up the GUI
root = tk.Tk()
root.title('Rock Paper Scissors')

# Add a label to display the outcome of each game and the scores
outcome_label = tk.Label(root, text='Make your move!')
outcome_label.pack()

# Add buttons for the player to choose their move
rock_button = tk.Button(root, text='Rock', command=lambda: play('rock'))
rock_button.pack()
paper_button = tk.Button(root, text='Paper', command=lambda: play('paper'))
paper_button.pack()
scissors_button = tk.Button(root, text='Scissors', command=lambda: play('scissors'))
scissors_button.pack()

# Start the GUI
root.mainloop()
