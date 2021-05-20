import turtle
from tkinter import messagebox, simpledialog, Tk
import math
import turtle

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
num = simpledialog.askinteger("Enter a radius",None)
    # Make a new turtle
Shivam = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
Shivam.circle(num)
    # Call the turtle .penup() method
Shivam.penup()
    # Move your turtle to a new x,y position using .goto()
Shivam.goto(100,80)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
arnum = math.pi*num*num
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
Shivam.write(arg="area = " + str(arnum), move=True, align='left', font=('Arial',8,'normal'))
    # Hide your turtle
Shivam.hideturtle()
    # Call turtle.done()
turtle.done()