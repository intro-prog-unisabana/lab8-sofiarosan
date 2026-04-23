"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys

if len(sys.argv) != 3:
    print("Error: Invalid input! Enter numeric values only.")
    sys.exit()
Carga= sys.argv[1]
Puntos= sys.argv[2]

if not Carga.isdigit() or not Puntos.isdigit():
    print("Error: Invalid input! Enter numeric values only.")
    sys.exit()
carga = float(Carga)
puntos= float(Puntos)

if puntos== 0:
    print("Error: Cannot divide by zero! Supports must be greater than zero.")
else:
    value= carga/puntos
    print(f"Load per support point: {value} N")