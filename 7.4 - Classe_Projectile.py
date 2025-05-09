# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 11:15:12 2025

@author: gusta
"""

# cball_animation1.py

# single-shot cannonball animation

from graphics import GraphWin, Text, Point, Entry, Circle, Line, update
from classeProjectile import Projectile, InputDialog, ShotTracker, Button






def main():

    # create animation window
    win = GraphWin("Projectile Animation", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)
    Line(Point(-10, 0), Point(210, 0)).draw(win)
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    angle, vel, height = 45.0, 40.0, 2.0
    
    # interact with the user
    inputwin = InputDialog(angle, vel, height)
    
    
    # event loop
    while True:
        # interact with the user
        choice = inputwin.interact()

        if choice == "Quit":  # loop exit
            break

        # otherwise choice is "Fire!"
        # create a shot and track until it hits ground or leaves window
        angle, vel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1/50)
            update(50)

    win.close()


if __name__ == "__main__":
    main()