#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  9 12:45:05 2025

@author: Rita Fernandes e Miguel Pascoal
"""

def calcular_consumo(filename):
    try:
        with open(filename, 'r') as file:
            linhas = file.readlines()

        # Valor inicial do odómetro
        odometro_inicial = float(linhas[0].strip())
        total_distancia = 0
        total_combustivel = 0

        print("Consumo por trajeto (L/100Km):")
        for linha in linhas[1:]:
            odometro_final, combustivel = map(float, linha.strip().split())
            distancia = odometro_final - odometro_inicial
            if distancia <= 0:
                print("Erro: distância inválida.")
                return
            consumo_100km = (combustivel / distancia) * 100
            print(f"Trajeto de {distancia:.1f} km: {consumo_100km:.2f} L/100Km")

            total_distancia += distancia
            total_combustivel += combustivel
            odometro_inicial = odometro_final  # Atualiza para o próximo trajeto

        # Consumo médio da viagem toda
        consumo_medio_total = (total_combustivel / total_distancia) * 100
        print(f"\nConsumo médio total: {consumo_medio_total:.2f} L/100Km")

    except FileNotFoundError:
        print("Erro: Ficheiro não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

# Substitui 'dados.txt' pelo nome do teu ficheiro
calcular_consumo('dados.txt')