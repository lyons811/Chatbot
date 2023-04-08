import openai
import tkinter as tk
from tkinter import scrolledtext

openai.api_key = "your-api-key-here"

messages = []


def send_message():
    message = user_input.get("1.0", tk.END).strip()
    if message:
        messages.append({"role": "user", "content": message})
        chat_box.insert(tk.END, f"User: {message}\n\n")  # Add extra space after the message
        user_input.delete("1.0", tk.END)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        chat_box.insert(tk.END, f"Assistant: {reply}\n\n")  # Add extra space after the message


def create_chatbot():
    system_msg = system_input.get()
    messages.append({"role": "system", "content": system_msg})
    chat_box.insert(tk.END, f"System: {system_msg}\nSay hello to your new assistant!\n\n")  # Add extra space after the message
    system_input.delete(0, tk.END)


def toggle_dark_mode():
    if root["bg"] == "#4f4f4f":
        dark_mode = False
        root.config(bg="#f0f0f0")
        chat_box.config(bg="white", fg="black", highlightbackground="white")
        user_input.config(bg="white", fg="black", highlightbackground="white")
    else:
        dark_mode = True
        root.config(bg="#4f4f4f")
        chat_box.config(bg="black", fg="white", highlightbackground="black")
        user_input.config(bg="black", fg="white", highlightbackground="black")

    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.config(bg=root["bg"], fg="black" if not dark_mode else "white")


root = tk.Tk()
root.title("Chatbot")

system_label = tk.Label(root, text="What type of chatbot would you like to create?")
system_label.pack()
system_input = tk.Entry(root, width=50)
system_input.pack()
system_button = tk.Button(root, text="Create", command=create_chatbot)
system_button.pack()

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, bg="white", fg="black")
chat_box.pack()

user_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, bg="white", fg="black")
user_input.pack()
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

toggle_dark_mode_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
toggle_dark_mode_button.pack()

root.mainloop()