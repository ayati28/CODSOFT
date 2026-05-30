import tkinter as tk
import random

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

def start_game(user_choice):
    global selected_choice
    selected_choice = user_choice

    result_label.config(text="")
    computer_label.config(text="")
    countdown(0)

def countdown(step):
    messages = ["🪨 Rock...", "📄 Paper...", "✂️ Scissors...", "🎯 Shoot!"]

    if step < len(messages):
        result_label.config(text=messages[step])
        root.after(700, lambda: countdown(step + 1))
    else:
        play_round()

def play_round():
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text=f"👤 You: {selected_choice}")
    computer_label.config(text=f"💻 Computer: {computer_choice}")

    if selected_choice == computer_choice:
        result = "🤝 It's a Tie!"

    elif (
        (selected_choice == "Rock" and computer_choice == "Scissors") or
        (selected_choice == "Paper" and computer_choice == "Rock") or
        (selected_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        user_score += 1

    else:
        result = "😢 Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"📊 Score  |  You: {user_score}   Computer: {computer_score}"
    )

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x450")

title = tk.Label(
    root,
    text="🎮 Rock Paper Scissors",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

tk.Label(
    root,
    text="Choose your move",
    font=("Arial", 12)
).pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="🪨 Rock",
    width=12,
    command=lambda: start_game("Rock")
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="📄 Paper",
    width=12,
    command=lambda: start_game("Paper")
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="✂️ Scissors",
    width=12,
    command=lambda: start_game("Scissors")
).grid(row=0, column=2, padx=5)

user_label = tk.Label(root, text="", font=("Arial", 12))
user_label.pack(pady=10)

computer_label = tk.Label(root, text="", font=("Arial", 12))
computer_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=20)

score_label = tk.Label(
    root,
    text="📊 Score  |  You: 0   Computer: 0",
    font=("Arial", 12)
)
score_label.pack(pady=15)

root.mainloop()