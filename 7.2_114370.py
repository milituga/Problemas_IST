#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  1 14:38:45 2025

@author: RI
"""

class Cubo:
    #definir a aresta do cubo
    def __init__(self, aresta):
        self.aresta = aresta  

    #definir o return value da aresta
    def getRadius(self):
        return self.aresta

    #definir a formula para obter a area da face do cubo
    def faceArea(self):
        return self.aresta ** 2

    #definir a formula para obter a area da superficie do cubo
    def surfaceArea(self):
        return 6 * (self.aresta ** 2)

    #definir a formula do volume do cubo
    def volume(self):
        return self.aresta ** 3


def main():
    try:
        #receber o valor da aresta para os calculos, verificando que o valor é válido
        aresta = float(input("Digite a aresta do cubo: "))
        cubo = Cubo(aresta)

        #mostrar ao utilizador os vários calculos
        print(f"\nAresta: {cubo.getRadius():.1f}")
        print(f"Área da face: {cubo.faceArea():.1f}")
        print(f"Área superficial: {cubo.surfaceArea():.1f}")
        print(f"Volume: {cubo.volume():.1f}")
        
    #caso o valor não seja válido aparece para digitar outro valor
    except ValueError:
        print("Erro: digite um número válido.")

if __name__ == "__main__":
    main()
