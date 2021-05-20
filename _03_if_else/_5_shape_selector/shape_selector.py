import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    Shivam = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    str = simpledialog.askstring("Do you want a triangle, square, or circle?", None)
    # Draw the shape requested by the user using if-elif-else statements
    if str == ("triangle"):
        Shivam.pendown()
        Shivam.forward(100)
        Shivam.left(120)
        Shivam.forward(100)
        Shivam.left(120)
        Shivam.forward(100)
    elif str == ("square"):
        Shivam.pendown()
        Shivam.forward(100)
        Shivam.right(90)
        Shivam.forward(100)
        Shivam.right(90)
        Shivam.forward(100)
        Shivam.right(90)
        Shivam.forward(100)
        Shivam.right(90)
    elif str == ("cirlce"):
        Shivam.pendown()
        Shivam.circle(10)


    # Call the turtle .done() method
    turtle.done()