# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:32:56 2025

@authors: Miguel Pascoal and Rita Fernandes
"""


# Import the library tkinter
import tkinter as tk


"""
Create the main window, which is where all the GUI components
will be placed. Then set a title for the window
"""
root = tk.Tk()
root.title("Rectangle drawer")


# Create a Canvas widget in which the user will draw the rectangle
# The width and height must be the same in order to be a square canvas
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()


# Create labels to display area and perimeter

# Begin with the Area
area_label = tk.Label(root, text="Area: 0", font=("Arial", 14))
area_label.pack()

# And then the perimeter
perimeter_label = tk.Label(root, text="Perimeter: 0", font=("Arial", 14))
perimeter_label.pack()


# Create the variables to store the first and second click positions
start_x, start_y = None, None


# Create the function that will detect the mouse clicks
def on_click(event):
    global start_x, start_y
    
    if start_x is None and start_y is None:
        # First click: Store the starting coordinates
        start_x, start_y = event.x, event.y
        print(f"First click at ({start_x}, {start_y})")
    else:
        # Second click: Store the ending coordinates
        end_x, end_y = event.x, event.y
        print(f"Second click at ({end_x}, {end_y})")

        # Draw the rectangle
        canvas.create_rectangle(start_x, start_y, end_x, end_y, outline="blue", width=2)
        
        # Calculate the area and perimeter
        width = abs(end_x - start_x)
        height = abs(end_y - start_y)
        area = width * height
        perimeter = 2 * (width + height)

        # Update the labels with the calculated values
        area_label.config(text=f"Area: {area}")
        perimeter_label.config(text=f"Perimeter: {perimeter}")
        
        # Reset start coordinates for the next rectangle
        start_x, start_y = None, None

# Bind the lmb (left mouse button) click to the function
canvas.bind("<Button-1>", on_click)

# Start the tkinter main loop to run the window
root.mainloop()
