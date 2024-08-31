import tkinter as tk
import random
import string

# defining Required functions

# Generate a random password based on user input


def generate_password(num_letters, num_digits, num_symbols):

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password_chars = (
            random.choices(letters, k=num_letters) +
            random.choices(digits, k=num_digits) +
            random.choices(symbols, k=num_symbols)
    )

    random.shuffle(password_chars)

    return ''.join(password_chars)


def on_generate():
    """Handle the password generation and update the text box."""
    try:
        num_letters = int(letters_entry.get())
        num_digits = int(digits_entry.get())
        num_symbols = int(symbols_entry.get())

        if num_letters < 0 or num_digits < 0 or num_symbols < 0:
            password_var.set("Please enter non-negative numbers.")
            return

        password = generate_password(num_letters, num_digits, num_symbols)
        password_var.set(password)
    except ValueError:
        password_var.set("Please enter valid numbers.")


# Create the main window
root = tk.Tk()
root.geometry("700x400")
root.title("Random Password Generator")

# Heading
tk.Label(text="Welcome To Password Generator", relief="sunken",
         font="comicsansms 15 bold", borderwidth=6, background="grey25", fg="white").grid(row=0, column=2)


# Creating Background
root["bg"] = "magenta4"

# Create a StringVar to hold the password
password_var = tk.StringVar()

# Create and place the widgets
tk.Label(root, text="Number of Letters:", relief="sunken", borderwidth=6,
         background="grey25", fg="white", font='comicsansms 10 bold', padx=23, pady=3).grid(row=1, column=1, padx=5, pady=10)
letters_entry = tk.Entry(root, relief="sunken", borderwidth=5,
                         background="grey40", fg="white", font='comicsansms 10 bold')
letters_entry.grid(row=1, column=2, padx=5, pady=10)
letters_entry.insert(0, "4")  # Default value

tk.Label(root, text="Number of Digits:", relief="sunken",  borderwidth=6,
         background="grey25", fg="white", font='comicsansms 10 bold', padx=22, pady=3).grid(row=2, column=1, padx=5, pady=10)
digits_entry = tk.Entry(root, relief="sunken", borderwidth=5, background="grey40", fg="white", font='comicsansms 10 bold')
digits_entry.grid(row=2, column=2, padx=5, pady=10)
digits_entry.insert(0, "3")  # Default value

tk.Label(root, text="Number of Symbols:", relief="sunken",  borderwidth=6, background="grey25", fg="white", font='comicsansms 10 bold', padx=20, pady=3).grid(row=3, column=1, padx=5, pady=10)
symbols_entry = tk.Entry(root, relief="sunken", borderwidth=5, background="grey40", fg="white", font='comicsansms 10 bold')
symbols_entry.grid(row=3, column=2, padx=5, pady=10)
symbols_entry.insert(0, "1")  # Default value

generate_button = tk.Button(root, text="Generate Password", relief="sunken", command=on_generate, borderwidth=5., background="grey40", fg="white", font='comicsansms 10 bold')
generate_button.grid(row=6, column=2, padx=5, pady=10)

password_entry = tk.Entry(root, textvariable=password_var, width=50, borderwidth=5., background="grey40", fg="white", font='comicsansms 10 bold')
password_entry.grid(row=7, column=2, padx=5, pady=10)

# Start the Tkinter event loop
root.mainloop()

# Name
T = tk.Text(root, height=2, width=20)
T.insert( "Developed by Aditya@17")
T.grid(row=9, column=0)
