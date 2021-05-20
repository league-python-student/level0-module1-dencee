from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
num = simpledialog.askstring("What color tomato would you like? (Red,Green,Blue)",None)

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if num == ("Red"):
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
elif num == ("Green"):
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")
elif num == ("Blue"):
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")




root.mainloop()
