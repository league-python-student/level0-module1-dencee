# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import tkinter as tk
import turtle
import math
from tkinter import messagebox, simpledialog, Tk
window_width = 600
window_height = 600

root = tk.Tk()
num = simpledialog.askinteger("Enter number for the radius of a circle",None)
str = simpledialog.askstring("Would you like to calculate the area or circumference of a circle?",None)
if str == ("area"):
    print(math.pi*num*num)
if str == ("circumference"):
    print(math.pi * num * 2)
#Area = πr^2
#Circumference = 2πr
