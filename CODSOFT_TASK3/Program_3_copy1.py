import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Frame for input
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=20)

        # Length Label and Entry
        self.length_label = tk.Label(self.input_frame, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=5)
        self.length_entry = tk.Entry(self.input_frame, width=5)
        self.length_entry.grid(row=0, column=1, padx=5)

        # Character Type Checkboxes
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        self.uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=self.include_uppercase)
        self.uppercase_checkbox.pack(anchor=tk.W)

        self.lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=self.include_lowercase)
        self.lowercase_checkbox.pack(anchor=tk.W)

        self.digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=self.include_digits)
        self.digits_checkbox.pack(anchor=tk.W)

        self.symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols)
        self.symbols_checkbox.pack(anchor=tk.W)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        # Copy Button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be positive.")
        except ValueError:
            self.result_label.config(text="Please enter a valid length.")
            return

        # Define character set based on selections
        characters = ""
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_lowercase.get():
            characters += string.ascii_lowercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_symbols.get():
            characters += string.punctuation

        if not characters:
            self.result_label.config(text="Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_label.config(text=f"Generated Password: {password}")

    def copy_to_clipboard(self):
        password = self.result_label.cget("text").replace("Generated Password: ", "")
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()  # Keeps the clipboard updated
            self.result_label.config(text="Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
