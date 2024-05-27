import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = int(length_entry.get())
    if length < 6:
        messagebox.showerror("Error", "Password length should be at least 6 characters.")
        return
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    generated_password_entry.config(state="normal")
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.insert(tk.END, password)
    generated_password_entry.config(state="readonly")
    update_generated_strength_meter(password)


def update_generated_strength_meter(password):
    strength = calculate_strength(password)
    generated_strength_label.config(text=f"Generated Password Strength: {strength}/16")


def update_manually_entered_strength_meter(password):
    strength = calculate_strength(password)
    manually_entered_strength_label.config(text=f"Manually Entered Password Strength: {strength}/16")


def calculate_strength(password):
    length = len(password)
    complexity = 0
    if any(c.isdigit() for c in password):
        complexity += 1
    if any(c.islower() for c in password):
        complexity += 1
    if any(c.isupper() for c in password):
        complexity += 1
    if any(c in string.punctuation for c in password):
        complexity += 1

    strength = min(length // 6, 4) * min(complexity, 4)
    return strength


def check_manually_entered_strength():
    password = password_entry.get()
    update_manually_entered_strength_meter(password)


root = tk.Tk()
root.title("Password Generator & Strength Checker")

# Password Generator Section
generator_frame = tk.LabelFrame(root, text="Password Generator", padx=10, pady=10)
generator_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

length_label = tk.Label(generator_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(generator_frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = tk.Button(generator_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

generated_password_label = tk.Label(generator_frame, text="Generated Password:")
generated_password_label.grid(row=2, column=0, padx=5, pady=5)

generated_password_entry = tk.Entry(generator_frame, state="readonly")
generated_password_entry.grid(row=2, column=1, padx=5, pady=5)

generated_strength_label = tk.Label(generator_frame, text="Generated Password Strength: 0/16")
generated_strength_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Password Strength Checker Section
checker_frame = tk.LabelFrame(root, text="Password Strength Checker", padx=10, pady=10)
checker_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

password_label = tk.Label(checker_frame, text="Enter Password:")
password_label.grid(row=0, column=0, padx=5, pady=5)

password_entry = tk.Entry(checker_frame, show="*")
password_entry.grid(row=0, column=1, padx=5, pady=5)

check_button = tk.Button(checker_frame, text="Check Strength", command=check_manually_entered_strength)
check_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

manually_entered_strength_label = tk.Label(checker_frame, text="Manually Entered Password Strength: 0/16")
manually_entered_strength_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
