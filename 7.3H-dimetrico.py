# -*- coding: utf-8 -*-
"""
Created on Fri May  2 11:12:14 2025

@author: Miguel Pascoal e Rita Fernandes
"""

from graphics import *
import math

class Cubo:
    #Definir aresta do cubo
    def __init__(self, aresta):
        self.aresta = aresta  
        
    #Definir return value da aresta do cubo
    def getRadius(self):
        return self.arest
    
    #Definir área da face do cubo
    def faceArea(self):
        return self.aresta ** 2
    
    #Definir área de superfície do cubo
    def surfaceArea(self):
        return 6 * (self.aresta ** 2)
    
    #Definir volume do cubo
    def volume(self):
        return self.aresta ** 3
    
    def desenhar_dimetrico(self):
        #Criar janela para desenhar o cubo
        win = GraphWin("Cubo Dimétrico (inclinação 3:2, 50% dimensão)", 500, 500)
        win.setBackground("white")
        
        """
        Criar os ângulos entre os eixos do cubo
        Inclinação 3:2 => ângulo ≈ 33.69°
        """
        theta = math.atan(2 / 3)
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)

        dimensao = 0.5  #Dimensão de 50%

        def dimetric_point(x, y, z):
            # Aplicar dimensão antes da projeção
            x *= dimensao
            y *= dimensao
            z *= dimensao
            dx = (x - z) * cos_theta
            dy = ((x + z) * sin_theta) - y
            return Point(dx + 250, dy + 250)

        a = self.aresta
        
        #Coordenadas em 3D dos pontos
        pontos_3d = {
            'A': (0, 0, 0),
            'B': (a, 0, 0),
            'C': (a, 0, a),
            'D': (0, 0, a),
            'E': (0, a, 0),
            'F': (a, a, 0),
            'G': (a, a, a),
            'H': (0, a, a)}
        
        #Converter as coordenadas 3D em 2D
        pontos_2d = {letra: dimetric_point(*coords) for letra, coords in pontos_3d.items()}

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
        #Aresta definida pelo utilizador
        aresta = float(input("Digite a aresta do cubo: "))
        cubo = Cubo(aresta)
        
        #Informações a apresentar na consola
        print(f"\nAresta: {cubo.getRadius():.1f}")
        print(f"Área da face: {cubo.faceArea():.1f}")
        print(f"Área superficial: {cubo.surfaceArea():.1f}")
        print(f"Volume: {cubo.volume():.1f}")

        cubo.desenhar_dimetrico()
        
    except ValueError:
        #Se o valor da aresta for impossível inserir um novo valor
        print("Erro: digite um número válido.")

main()
