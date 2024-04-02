import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

root = tk.Tk()
root.title("Tkinter Example")

label = tk.Label(root, text="Hello, Tkinter!")
button = tk.Button(root, text="Click Me", command=on_button_click)

label.pack()
button.pack()

root.mainloop()
