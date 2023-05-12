# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:40:32 2023

@author: karun
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # set up the game window and title
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # set up variables for the players and the turn
        self.player1 = "X"
        self.player2 = "O"
        self.current_player = self.player1

        # set up variables for the game board
        self.board = ["", "", "", "", "", "", "", "", ""]

        # set up the game grid
        self.game_board = tk.Frame(self.window)
        self.game_board.pack()

        # create the buttons for the game board
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.game_board, text="", width=4, height=2, font=("Helvetica", 20), command=lambda index=i: self.button_click(index))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def start_game(self):
        # start the game loop
        self.window.mainloop()

    def button_click(self, index):
        # check if the button has already been clicked
        if self.buttons[index]['text'] == "":
            # mark the button with the current player's symbol
            self.buttons[index]['text'] = self.current_player

            # update the game board and check for a winner
            self.board[index] = self.current_player
            winner = self.check_winner()
            if winner:
                self.show_message("Player " + winner + " wins!")
                self.reset_game()
            elif self.is_board_full():
                self.show_message("It's a tie!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        # switch to the other player's turn
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def check_winner(self):
        # check for a winner in the rows, columns, and diagonals
        for i in range(3):
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != "":
                return self.board[i*3]
            elif self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return self.board[i]
        if self.board[0] == self.board[4] == self.board[8] != "":
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] != "":
            return self.board[2]
        else:
            return None

    def is_board_full(self):
        # check if the game board is full
        for i in self.board:
            if i == "":
                return False
        return True

    def reset_game(self):
        # reset the game board and buttons
        self.current_player = self.player1
        self.board = ["", "", "", "", "", "", "", "", ""]
        for button in self.buttons:
            button['text'] = ""

    def show_message(self, message):
        # show a message box with the given message
        messagebox.showinfo("Game Over", message)

# start the game
game = TicTacToe()
game.start_game()
