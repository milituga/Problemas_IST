# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tabulate import tabulate

# Firstly define the fuction

def main():
    
    #Define the data to use in the table
    dados = []
    
    #Create the actual values
    for c in range(0, 101, 10):
        f = c * 9/5 + 32
        dados.append([c, f]) # Criar os dados para a tabela
    
    #Print the table with the desired format
    print(tabulate(dados, headers=["Celsius (°C)", "Fahrenheit (°F)"], tablefmt="grid"))

main()
