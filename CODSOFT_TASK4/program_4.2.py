import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0
        self.max_score = 20
        self.username = ""

        # Username entry
        self.username_label = tk.Label(master, text="Enter your username:")
        self.username_label.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="nsew")

        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=1, column=0, columnspan=3, pady=(5, 10), sticky="nsew")

        # Instructions label
        self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors:")
        self.label.grid(row=2, column=0, columnspan=3, pady=(10, 5), sticky="nsew")

        # Buttons for user choices
        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("rock"), width=10)
        self.rock_button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("paper"), width=10)
        self.paper_button.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("scissors"), width=10)
        self.scissors_button.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

        # Result label
        self.result_label = tk.Label(master, text="", wraplength=300)
        self.result_label.grid(row=4, column=0, columnspan=3, pady=(5, 5), sticky="nsew")

        # Score label
        self.score_label = tk.Label(master, text="User: 0 | Computer: 0")
        self.score_label.grid(row=5, column=0, columnspan=3, pady=(5, 10), sticky="nsew")

        # Play Again button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.grid(row=6, column=0, columnspan=3, pady=(5, 5), sticky="nsew")

        # Exit button
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.grid(row=7, column=0, columnspan=3, pady=(5, 10), sticky="nsew")

        # Configure row and column weights for resizing
        for i in range(8):
            master.grid_rowconfigure(i, weight=1)
        for i in range(3):
            master.grid_columnconfigure(i, weight=1)

    def play(self, user_choice):
        self.username = self.username_entry.get().strip()
        if self.username == "":
            self.result_label.config(text="Please enter a username before playing.")
            return

        if self.user_score >= self.max_score or self.computer_score >= self.max_score:
            self.result_label.config(text="Game Over! Please reset to play again.")
            return

        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"{self.username} chose {user_choice}. Computer chose {computer_choice}. {result}")
        self.update_scores(result)

        if self.user_score >= self.max_score or self.computer_score >= self.max_score:
            if self.user_score >= self.max_score:
                self.result_label.config(text=f"{self.username} WINS! CONGRATULATIONS! Final Scores - {self.username}: {self.user_score}, Computer: {self.computer_score}")
            else:
                self.result_label.config(text=f"{self.username} LOSES! BETTER LUCK NEXT TIME! Final Scores - {self.username}: {self.user_score}, Computer: {self.computer_score}")
            
            self.play_again_button.config(state=tk.NORMAL)

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            return f"{self.username} wins!"
        else:
            return f"{self.username} loses!"

    def update_scores(self, result):
        if f"{self.username} wins!" in result:
            self.user_score += 1
        elif f"{self.username} loses!" in result:
            self.computer_score += 1

        self.score_label.config(text=f"{self.username}: {self.user_score} | Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.username_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.score_label.config(text="User: 0 | Computer: 0")
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
