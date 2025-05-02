# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:08:50 2025

@author: Rita Fernandes e Miguel Pascoal
"""

#facenew.py
from graphics import *

class Face:
    def __init__(self, window, center, size):
        self.size = size
        self.eyeSize = 0.15 * size
        self.eyeOff = size / 3.0
        self.mouthSize = 0.8 * size
        self.mouthOff = size / 2.0 
        self.center = center
        self.window = window
        self.initializeGrimFace()
        self.rightEye 
    
    def getCenter(self):
        return self.center

    def move(self, dx, dy):
        self.unDraw()
        center = self.getCenter()
        x = center.getX()
        y = center.getY()
        self.center = Point(x + dx, y + dy)
        if dx < 0 and dy < 0:
            self.smile()
        elif dx < 0 and dy > 1:
            self.wink()

        elif dx > 0 and dy > 0:
            self.initializeGrimFace()
                
        else:
            self.meditate()

    def initializeGrimFace(self):
        self.head = Circle(self.center, self.size)
        self.leftEyeOpen()
        self.rightEyeOpen()
        self.teeth = []
        self.lineMouth()
        self.drawFace()

    def lineMouth(self):
        p1 = self.center.clone()
        p1.move(-self.mouthSize/2, self.mouthOff)
        p2 = self.center.clone()
        p2.move(self.mouthSize/2, self.mouthOff)
        self.mouth = Line(p1, p2)
        return Line(p1, p2)

    def rectMouth(self):
        p1, p2 = self.mouth.getP1(), self.mouth.getP2()
        x1, x2, y1, y2 = p1.getX(), p2.getX(), p1.getY(), p2.getY()
        offset = self.eyeSize / 2
        self.mouth = Rectangle(Point(x1, y1 - offset), Point(x2, y2 + offset))
        return x1, x2, y1, y2, offset

    def unDraw(self):
        self.head.undraw()
        self.leftEye.undraw()
        self.rightEye.undraw()
        self.mouth.undraw()
        for tooth in self.teeth:
            tooth.undraw()

    def drawFace(self):
        self.head = Circle(self.center, self.size)
        self.head.draw(self.window)
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        self.mouth.draw(self.window)

    def leftEyeOpen(self):
        self.leftEye = Circle(self.center, self.eyeSize)
        self.leftEye.move(-self.eyeOff, -self.eyeOff)

    def rightEyeOpen(self):
        self.rightEye = Circle(self.center, self.eyeSize)
        self.rightEye.move(self.eyeOff, -self.eyeOff)
    
    def leftEyeWink(self):
        center = self.center #self.leftEye.getCenter()
        x = center.getX()
        y = center.getY()
        leftWink = Line(Point(x - self.eyeSize, y), Point(x + self.eyeSize, y))
        self.leftEye = leftWink
        self.leftEye.move(-self.eyeOff, -self.eyeOff)
    
    def rightEyeWink(self):
        center = self.center #rightEye.getCenter()
        x = center.getX()
        y = center.getY()
        rightWink = Line(Point(x - self.eyeSize, y), Point(x + self.eyeSize, y))
        self.rightEye = rightWink
        self.rightEye.move(self.eyeOff, -self.eyeOff)


    def wink(self):
        self.unDraw()
        self.lineMouth()
        self.leftEyeOpen()
        self.rightEyeWink()
        self.drawFace()

    def smile(self):
        self.unDraw()
        self.teeth=[]
        self.teeth.append(self.lineMouth())
        x1, x2, y1, y2, offset = self.rectMouth()
        xint = abs(x2 - x1) / 8
       
#        i=0
#        t2 = Line(Point(x1 + i * xint, y1 - offset), Point((x1 + i * xint), y2 + offset))
#        self.teeth.append(t2)
        for i in range (0,8):
            t2 = Line(Point(x1 + i * xint, y1 - offset), Point((x1 + i * xint), y2 + offset))
            self.teeth.append(t2)    
        for tooth in self.teeth:
            tooth.draw(self.window)
        self.rectMouth()
        self.leftEyeOpen()
        self.rightEyeOpen()

        self.drawFace()

    def meditate(self):
        self.unDraw()
        self.lineMouth()
        self.leftEyeWink()
        self.rightEyeWink()
        self.drawFace()

    def changeExpression(self, expression):
        """Changes the face expression based on hitting a wall."""
        self.unDraw()
        if expression == "smile":
            self.smile()
        elif expression == "wink":
            self.wink()
        else:
            self.lineMouth()
            self.leftEyeOpen()
            self.rightEyeOpen()
        self.drawFace()

    def changeColor(self, color):
        """Changes the face's color."""
        self.head.setFill(color)

# --- Bouncing Animation ---

def main():
    win = GraphWin("Bouncing Face", 500, 500)
    win.setCoords(-250, -250, 250, 250)
    win.setBackground("mistyrose")

    radius = 70
    face = Face(win, Point(50, -50), radius)

    dx, dy = 1, 1

    for _ in range(10000):
        c = face.center

        # Bounce off walls and change color + expression
        if c.getX() > 250 - radius:
            dx = -1
            face.changeColor("gold")
            face.changeExpression("smile")  
        elif c.getX() < - (250 - radius):
            dx = 1
            face.changeColor("aquamarine")
            face.changeExpression("wink")  
        if c.getY() > 250 - radius:
            dy = -1
            face.changeColor("fuchsia")
            face.changeExpression("neutral")  
        elif c.getY() < - (250 - radius):
            dy = 1
            face.changeColor("lightcoral")
            face.changeExpression("wink")  

        face.move(1 * dx, 1 * dy)
        update(60)
    win.close()

main()
