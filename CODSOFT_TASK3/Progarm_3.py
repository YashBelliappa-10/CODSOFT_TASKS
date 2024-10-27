import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Length Label
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=10)

        # Length Entry
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

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

        # Define character set for password
        characters = string.ascii_letters + string.digits + string.punctuation
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
