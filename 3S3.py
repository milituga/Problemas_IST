# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 16:26:32 2025

@author: Miguel Pascoal
"""

def main():
    x = eval(input("Introduza o número de quilos de café que pretende encomendar "))
    y = 3.36 * x + 1.50
    w = 0.23 * x
    z = y + w
    
    """
    x é o número de quilos a encomendar
    
    y é o preço da encomenda antes do IVA
    ou seja, o que o vendedor recebe
    
    w é o valor do IVA
    
    z é o preço a pagar pelo consumidor
    
    """
    print("-" * 30)
    print("Quantidade a encomendar: ", x,"kg")
    print(f"Valor antes de impostos: {y:.2f}€")
    print(f"Valor do IVA: {w:.2f}")
    print(f"Valor a pagar: {z:.2f}€")
    print("-" * 30)
    
main()
