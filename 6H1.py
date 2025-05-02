# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 17:15:58 2025

@author: Rita Fernandes e Miguel Pascoal
"""

from graphics import *

class BotaoCircular:
    def __init__(self, win, center, radius, label):
        self.center = center
        self.radius = radius
        self.active = False

        # Create the circular button
        self.circ = Circle(center, radius)
        self.circ.setFill('lightgray')
        self.circ.draw(win)

        # Create the label
        self.label = Text(center, label)
        self.label.draw(win)

        # Display center coordinates and radius
        self.info_text = Text(Point(center.getX(), center.getY() + radius + 20), f"Centro: ({center.getX()}, {center.getY()})\nRaio: {radius}")
        self.info_text.setSize(10)
        self.info_text.draw(win)


    def clicked(self, p):
        """Returns True if the button is active and p is inside the circle"""
        if not self.active:
            return False

        # Calculate the distance from the click point to the center
        dx = p.getX() - self.center.getX()
        dy = p.getY() - self.center.getY()
        distance = (dx**2 + dy**2) ** 0.5

        return distance <= self.radius

    def obter_label(self):
        """Returns the label text of this button"""
        return self.label.getText()

    def ativar(self):
        """Activates the button"""
        self.label.setFill('black')
        self.circ.setWidth(2)
        self.active = True

    def desativar(self):
        """Deactivates the button"""
        self.label.setFill('darkgrey')
        self.circ.setWidth(1)
        self.active = False

    def atualizar(self, win, label):
        """Updates the button label"""
        self.label.undraw()
        self.label = Text(self.center, label)
        self.label.draw(win)
        

def main():
    win = GraphWin("Teste Botão Circular", 400, 400)

    # Create a circular button at (200, 200) with radius 50
    botao = BotaoCircular(win, Point(200, 200), 50, "Clique")

    botao.ativar()  # Activate the button

    while True:
        click = win.getMouse()  # Wait for a mouse click
        if botao.clicked(click):
            botao.atualizar(win, "yes")
            print("Botão Clicado!")

    win.close()

main()

