import tkinter as tk
import random

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg='#A8E6CF')

num = random.randint(0, 25)
chance = 3  # Only provided with 3 chances
var = tk.IntVar()
disp = tk.StringVar()


def check_guess():
    global num
    global chance
    usr_ip = var.get()  # User input
    if chance > 0:
        if usr_ip == num:
            msg = f'You won! {num} is the right answer.'
            chance = 0  # End game
        elif usr_ip > num:
            chance -= 1
            msg = f'{usr_ip} is greater. You have {chance} attempt(s) left.'
        elif usr_ip < num:
            chance -= 1
            msg = f'{usr_ip} is smaller. You have {chance} attempt(s) left.'
        else:
            msg = 'Something went wrong.'
    else:
        msg = f'You Lost! The correct number was {num}.'

    disp.set(msg)


# Title Label
tk.Label(
    root,
    text="Guess the Number",
    font=('Georgia', 20),
    relief='groove',
    padx=10,
    pady=10,
    bg='#C5B9D7'
).pack(pady=(10, 0))

# Entry for User Input
tk.Entry(
    root,
    textvariable=var,
    font=('Georgia', 18)
).pack(pady=(50, 10))

# Submit Button
tk.Button(
    root,
    text="Submit Guess",
    font=("Georgia", 15),
    command=check_guess
).pack()

# Feedback Label
tk.Label(
    root,
    textvariable=disp,
    bg='#FF7F7F',
    font=('Georgia', 12),
    relief='ridge',
    wraplength=350,
    padx=10,
    pady=10
).pack(pady=(20, 0))

root.mainloop()
