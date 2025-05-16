# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: old_primes.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 18:42:35 UTC (1746556955)
"""
import os
lower = 1
upper = 50
os.system('clear')
print('Numeros primos entre %d y %d son: \n' % (lower, upper))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print('%d ' % num)
"""
import sys

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def obtener_primos(hasta):
    return [num for num in range(1, hasta + 1) if es_primo(num)]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python new_primes.py <número_máximo>")
        sys.exit(1)
    
    try:
        limite = int(sys.argv[1])
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        sys.exit(1)

    primos = obtener_primos(limite)
    print(f"Números primos entre 1 y {limite} son:\n")
    for p in primos:
        print(p)
