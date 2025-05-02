#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  1 14:28:00 2025

@author: Rita Fernandes e Miguel Pascoal
"""

import math

class Sphere:
    #definir o raio da esfera
    def __init__(self, radius):
        self.radius = radius
        
    #definir o return value do raio 
    def getRadius(self):
        return self.radius

    #definir o valor da area da superficie da esfera
    def surfaceArea(self):
        return 4 * math.pi * (self.radius ** 2)

    #definir o valor do volume 
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

def main():
    try:
        #receber o valor da aresta para os calculos, verificando que o valor é válido
        raio = float(input("Digite o raio da esfera: "))
        esfera = Sphere(raio)

        #mostrar ao utilizador os vários calculos
        print(f"\nRaio: {esfera.getRadius():.1f}")
        print(f"Área superficial: {esfera.surfaceArea():.1f}")
        print(f"Volume: {esfera.volume():.1f}")
        
    #caso o valor não seja válido aparece para digitar outro valor
    except ValueError:
        print("Erro: digite um número válido.")

if __name__ == "__main__":
    main()
