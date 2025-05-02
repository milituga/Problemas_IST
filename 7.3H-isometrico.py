# -*- coding: utf-8 -*-
"""
Created on Fri May  2 10:54:22 2025

@author: Miguel Pascoal e Rita Fernandes
"""

from graphics import *
import math

#Definir os parâmetros do cubo
class Cubo:
    
    #Valor da aresta do cubo
    def __init__(self, aresta):
        self.aresta = aresta  
    
    #Retornar o valor dado pelo utilizador
    def getRadius(self):
        return self.aresta
    
    #Calcular o valor da área a partir da aresta
    def faceArea(self):
        return self.aresta ** 2
    
    #Calcular o valor da area total de superficie
    def surfaceArea(self):
        return 6 * (self.aresta ** 2)
    
    #Calcular o valor do volume a partir da aresta
    def volume(self):
        return self.aresta ** 3
    
    #Desenhar o cubo
    def desenhar_isometrico(self):
        win = GraphWin("Cubo Isométrico com Profundidade 1:1", 500, 500)
        win.setBackground("white")

        #Constantes da projeção isométrica
        angle = math.radians(30)
        cos30 = math.cos(angle)
        sin30 = math.sin(angle)
        
        #Eixos x, y, z para o cubo
        def iso_point(x, y, z):
            iso_x = (x - z) * cos30
            iso_y = (x + z) * sin30 - y
            return Point(iso_x + 250, iso_y + 250)
        
        #Valor da aresta definido pelo utilizador
        a = self.aresta
        
        #Coordenadas para os pontos do cubo em 3D
        pontos_3d = {
            'A': (0, 0, 0),
            'B': (a, 0, 0),
            'C': (a, 0, a),
            'D': (0, 0, a),
            'E': (0, a, 0),
            'F': (a, a, 0),
            'G': (a, a, a),
            'H': (0, a, a),}
        
        #Converter as coordenadas 3D em pontos 2D para o graphics
        pontos_2d = {letra: iso_point(*coords) for letra, coords in pontos_3d.items()}

        arestas = [
            ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'),
            ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'E'),
            ('A', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H')]

        for inicio, fim in arestas:
            Line(pontos_2d[inicio], pontos_2d[fim]).draw(win)

        win.getMouse()
        win.close()


def main():
    try:
        #Pedir ao utilizador o valor da aresta
        aresta = float(input("Digite a aresta do cubo: "))
        cubo = Cubo(aresta)
        
        #Infromações para a consola
        print(f"\nAresta: {cubo.getRadius():.1f}")
        print(f"Área da face: {cubo.faceArea():.1f}")
        print(f"Área superficial: {cubo.surfaceArea():.1f}")
        print(f"Volume: {cubo.volume():.1f}")

        cubo.desenhar_isometrico()
    
    #Se for impossível pedir novo valor para a aresta
    except ValueError:
        print("Erro: digite um número válido.")

main()
