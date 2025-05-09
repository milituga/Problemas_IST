# -*- coding: utf-8 -*-
"""
Created on Tue May 06 11:05:56 2025

@author: Miguel Pascoal e Rita Fernandes
"""

from graphics import *

class GraphicsGroup:
    def __init__(self, anchor):
        self.anchor = anchor
        self.group = []
        
    def getAnchor(self):
        return self.anchor
    
    def addObject(self, gObject):
        self.group.append(gObject)
        
    # Moves the group to a new x/y
    def move(self, new_x, new_y):
        # Calculates the difference from the current anchor position
        dx = new_x - self.anchor.getX()
        dy = new_y - self.anchor.getY()
        
        # Updates the anchor position
        self.anchor.move(dx, dy)
        
        # Moves all objects in the group
        for graphics_object in self.group:
            graphics_object.move(dx, dy)
    
    def draw(self, win):
        for graphics_object in self.group:
            graphics_object.draw(win)
            
    def undraw(self):
        for graphics_object in self.group:
            graphics_object.undraw()
            
def eyes(center, size):
    eyeSize = .15 * size
    eyeOff = size / 3.0
    
    leftEye = Circle(center, eyeSize)
    leftEye.move(-eyeOff, eyeOff)
    
    rightEye = Circle(center, eyeSize)
    rightEye.move(eyeOff, eyeOff)
    return leftEye, rightEye

def mouth(center, size):
    mouthWidth = 0.6 * size
    mouthHeight = 0.2 * size
    leftMouth = Point(center.getX() - mouthWidth / 2, center.getY() - mouthHeight)
    rightMouth = Point(center.getX() + mouthWidth / 2, center.getY() - mouthHeight)
    
    smile = Line(leftMouth, rightMouth)
    smile.setOutline("black")
    smile.setWidth(2)
    
    return smile

def main():
    win = GraphWin("Moving face", 400, 400)
    win.setCoords(0, 0, 10, 10)
    center = Point(5, 5)
    face = GraphicsGroup(center)
    head = Circle(face.getAnchor(), 1.2)
    leftEye, rightEye = eyes(face.getAnchor(), 1.2)
    smile = mouth(face.getAnchor(), 1.2)
    
    for i in [leftEye, rightEye, smile, head]:
        face.addObject(i)
    
    face.draw(win)
    print(face.getAnchor())
    
    # Waits for mouse clicks to move the face
    while True:
        click_point = win.getMouse()  # Gets the mouse click point
        face.move(click_point.getX(), click_point.getY())  # Moves face to where the user clicks

main()
