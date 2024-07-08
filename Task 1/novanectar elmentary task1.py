import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import hashlib
import logging

# Setup logging
logging.basicConfig(filename='security.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Caesar cipher encryption
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            else:
                encrypted += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            encrypted += char 
    return encrypted

# Caesar cipher decryption
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Create a simple user database
users = {
    "admin": hashlib.sha256("password123".encode()).hexdigest()
}

# Authenticate user
def authenticate(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username] == hashed_password:
            return True
        else:
            logging.warning("Suspicious activity: Failed login attempt for user %s", username)
            return False
    else:
        logging.warning("Suspicious activity: Failed login attempt for user %s", username)
        return False

# Function to display message boxes on the right side of the screen
def right_side_messagebox(msg_type, title, message):
    # Get the dimensions of the screen and window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 300  # Approximate width of messagebox
    window_height = 150  # Approximate height of messagebox

    # Calculate position
    x = screen_width - window_width - 50  # 50 pixels from the right edge
    y = (screen_height // 2) - (window_height // 2)

    # Create a top-level window to position the messagebox
    top = tk.Toplevel(root)
    top.withdraw()  # Hide the window
    top.geometry(f"{window_width}x{window_height}+{x}+{y}")
    top.update_idletasks()
    top.deiconify()  # Show the window

    if msg_type == "info":
        messagebox.showinfo(title, message, parent=top)
    elif msg_type == "error":
        messagebox.showerror(title, message, parent=top)

    top.destroy()  # Destroy the top-level window after showing the messagebox

# GUI functions
def login():
    username = username_entry.get()
    password = password_entry.get()

    if authenticate(username, password):
        right_side_messagebox("info", "Login", "Authentication successful!")
        encryption_frame.pack(fill="both", expand=True)
    else:
        right_side_messagebox("error", "Login", "Authentication failed!")

def encrypt_message():
    message = message_entry.get()
    shift = int(shift_entry.get())
    encrypted = caesar_encrypt(message, shift)
    right_side_messagebox("info", "Encrypted Message", f"Encrypted: {encrypted}")

def decrypt_message():
    encrypted_message = message_entry.get()
    shift = int(shift_entry.get())
    decrypted = caesar_decrypt(encrypted_message, shift)
    right_side_messagebox("info", "Decrypted Message", f"Decrypted: {decrypted}")

# GUI setup
root = tk.Tk()
root.title("Encryption and Authentication")

# Center the main window
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Username").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

encryption_frame = tk.Frame(root)
tk.Label(encryption_frame, text="Message").grid(row=0, column=0)
message_entry = tk.Entry(encryption_frame)
message_entry.grid(row=0, column=1)

tk.Label(encryption_frame, text="Shift").grid(row=1, column=0)
shift_entry = tk.Entry(encryption_frame)
shift_entry.grid(row=1, column=1)

encrypt_button = tk.Button(encryption_frame, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=2, column=0)

decrypt_button = tk.Button(encryption_frame, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=2, column=1)

root.mainloop()
