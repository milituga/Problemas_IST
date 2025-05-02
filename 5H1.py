# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 19:25:38 2025

@author: Miguel Pascoal, Rita Fernandes
"""

from graphics import *

def main():
    win = GraphWin("Animated Circle", 500, 500)
    win.setCoords(-250, -250, 250, 250)
    
    radius = 70
    shape = Circle(Point(10, -80), radius)
    def set_color(color = "lightcoral"):
        shape.setFill(color)
    
    shape.setOutline("dimgrey")
    set_color("lightcoral")
    shape.draw(win)
    
    dx = 1
    dy = 1
    
    win.setBackground("mistyrose")  # Background color for better visibility
    for i in range(10000):
        c = shape.getCenter()
        
        # Reverse direction if the circle hits window boundaries
        if c.getX() > 250 - radius:
            dx = -1
            set_color("gold")
        elif c.getX() < - (250 - radius):
            dx = 1
            set_color("aquamarine")
        if c.getY() > 250 - radius:
            dy = -1
            set_color("fuchsia")
        elif c.getY() < - (250 - radius):
            dy = 1
            set_color("lightcoral")
        
        shape.move(1.1 * dx, 1.3 * dy)
        update(60)  # Limit the frame rate to 60 FPS
        
        if win.checkMouse():  # Close window if mouse is clicked
            break

    win.close()  # Close the window when the loop ends

main()
