import tkinter as tk
from tkinter import filedialog
import socket


# Data to be sent - hardcoded value for now  - can change to the data read from file
# data = input("Enter data to send: ").encode()

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r') as file:
               data = file.read()
               send_data(data)
        except:
            print("Error reading file")


def send_data(data):
    # Configuration
    HOST = 'localhost'
    PORT = 8000
    # Connect to Microservice 2
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.connect((HOST, PORT))
    print("Sending data:", data)
    receiver_socket.sendall(data.encode())
    receiver_socket.close()
    

def send_manually():
    data = text_entry.get("1.0", tk.END).strip()
    if data:
        send_data(data)

def clear_placeholder(event):
    if text_entry.get("1.0", tk.END).strip() == placeholder_text:
        text_entry.delete("1.0", tk.END)
        text_entry.configure(fg="black")

# Create the main window
window = tk.Tk()
window.title("Data Transfer!!") 
# Select file button
file_button = tk.Button(window, text="Select File", command=select_file)
file_button.pack()

# CText area
placeholder_text = "Type your data here"
text_entry = tk.Text(window, height=10, width=50,fg="gray")
text_entry.insert(tk.END, placeholder_text)
text_entry.bind("<FocusIn>", clear_placeholder)
text_entry.pack()

# Create the Send Manually button
send_button = tk.Button(window, text="Send Manually", command=send_manually)

send_button.pack()
window.mainloop()
