import time
import string
import random
from customtkinter import *

current_time = time.time()
random.seed(current_time)
play = False

# show top level menu
class TopMenu(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("300x300")
        self.title("Main Menu")
        self.focus_force()
        self.label = CTkLabel(self, text="Welcome", font=("Helvetica", 28, "bold"), text_color="#E5E5E5")
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        
        self.startBtn = CTkButton(self, text="Play", command=self.start_game)
        self.startBtn.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        self.quitBtn = CTkButton(self, text="Quit", command=self.quit_game)
        self.quitBtn.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    
    def start_game(self):
        global play
        play = True
        self.destroy()

    def quit_game(self):
        self.destroy()
        app.destroy()

# game clock
class GameTimer(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.timerValue = 60 * 3
        self.turns = 3
        self.windowTimer = CTkLabel(self, text="Starting...", font=("Helvetica", 28, "bold"), text_color="#E5E5E5")
        self.windowTimer.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

    def countDown(self):
        global play
        if play:
            if self.turns > 0:
                if self.timerValue >= 0:
                    mins, secs = divmod(self.timerValue, 60)
                    self.windowTimer.configure(text=f'Turns Left {self.turns} | Timer: {mins:02d}:{secs:02d}')
                    self.timerValue -= 1
                else:
                    self.turns -= 1
                    self.timerValue = 60 * 3
            else:
                play = False  # End game when turns run out
                self.windowTimer.configure(text="Game Over")
        self.after(1000, self.countDown)

# boggle board
class BoggleBoard:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def find_words(self, word):
        word = word.upper()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.find_from_position(word, i, j, set()):
                    return True
        return False

    def find_from_position(self, word, row, col, used):
        if not word:
            return True
        if (row < 0 or row >= self.rows or col < 0 or col >= self.cols or 
            (row, col) in used or self.board[row][col] != word[0]):
            return False
        used.add((row, col))
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dx, dy in directions:
            if self.find_from_position(word[1:], row + dx, col + dy, used.copy()):
                return True
        return False

class BoggleDisplay(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#2B2B2B", corner_radius=15, border_width=2, border_color="#404040")
        self.gameTimer = 0
        self.uppercase_alphabet = string.ascii_uppercase
        self.current_board = []
        self.create_new_board()

    def create_new_board(self):
        self.current_board = []
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        for x in range(4):
            row = []
            for y in range(4):
                letter = random.choice(self.uppercase_alphabet)
                row.append(letter)
                letter_frame = CTkFrame(self, width=40, height=40, fg_color="#3B3B3B", corner_radius=10)
                letter_frame.grid(row=x, column=y, padx=4, pady=4, sticky="nsew")
                buttonLetter = CTkLabel(letter_frame, text=letter, font=("Helvetica", 16, "bold"), text_color="#E5E5E5")
                buttonLetter.place(relx=0.5, rely=0.5, anchor="center")
            self.current_board.append(row)
        self.boggle_board = BoggleBoard(self.current_board)
        self.after(1000 * self.gameTimer, self.create_new_board)

class UserPoints(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.totalPoints = 0
        self.userPoints = CTkLabel(self, text="Points: 0", font=("Helvetica", 24, "bold"), text_color="#E5E5E5")
        self.userPoints.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    
    def calculate_points(self, word):
        points = 0
        word_length = len(word)
        if word_length >= 3:
            if word_length == 3 or word_length == 4:
                points = 1
            elif word_length == 5:
                points = 2
            elif word_length == 6:
                points = 3
            elif word_length == 7:
                points = 5
            else:
                points = 11
        self.totalPoints += points
        self.update_points_display()

    def update_points_display(self):
        self.userPoints.configure(text=f"Points: {self.totalPoints}")

class UserInput(CTkFrame):
    def __init__(self, master, boggle_board, user_points):
        super().__init__(master, fg_color="transparent")
        self.gameTimer = 0
        self.boggle_board = boggle_board
        self.user_points = user_points
        self.label = CTkLabel(self, text="Enter your words:", font=("Helvetica", 16), text_color="#E5E5E5")
        self.label.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="w")
        self.entry = CTkTextbox(self, height=100, width=400, font=("Helvetica", 16), border_width=2, border_color="#404040", fg_color="#2B2B2B", text_color="#E5E5E5")
        self.entry.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    def updateText(self):
        global play
        if play:
            self.entry.delete("0.0","end")
        self.after(1000 * self.gameTimer, self.updateText)

def setup_window():
    app = CTk()
    app.title("Boggle")
    app.geometry("600x600")
    app.configure(fg_color="#1B1B1B")

    menu = TopMenu(app)
    title = CTkLabel(app, text="BOGGLE", font=("Helvetica", 40, "bold"), text_color="#E5E5E5")
    title.grid(row=0, column=0, padx=20, pady=(30, 20))

    gameTimer = GameTimer(app)
    gameTimer.grid(row=1, column=0, pady=10)

    boggleDisplay = BoggleDisplay(app)
    boggleDisplay.grid(row=2, column=0, padx=50, pady=30)

    userPoints = UserPoints(app)
    userPoints.grid(row=3, column=0, pady=10)

    userInput = UserInput(app, boggleDisplay.boggle_board, userPoints)
    userInput.grid(row=4, column=0, padx=20, pady=20)

    # update
    userInput.gameTimer = gameTimer.timerValue
    boggleDisplay.gameTimer = gameTimer.timerValue
    gameTimer.countDown()
    userInput.updateText()
    userPoints.calculate_points(userInput.entry.get("0.0", "end"))
    boggleDisplay.create_new_board()
    return app

if __name__ == "__main__":
    app = setup_window()
    app.mainloop()