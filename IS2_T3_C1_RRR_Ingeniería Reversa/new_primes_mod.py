import sys

def es_primo(num):
    """
    Determina si un número es primo.
    
    Parámetros:
        num (int): Número a verificar.
    
    Retorna:
        bool: True si es primo, False en caso contrario.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def obtener_primos(hasta):
    """
    Devuelve una lista de números primos entre 1 y 'hasta' (inclusive).
    
    Parámetros:
        hasta (int): Límite superior del rango.
    
    Retorna:
        list: Lista de números primos.
    """
    return [n for n in range(1, hasta + 1) if es_primo(n)]

def main():
    """
    Función principal que gestiona la entrada desde la línea de comandos.
    """
    if len(sys.argv) != 2:
        print("Uso: python new_primes_mod.py <número_límite>")
        sys.exit(1)
    
    try:
        limite = int(sys.argv[1])
        if limite < 1:
            raise ValueError
    except ValueError:
        print("Por favor, ingrese un número entero positivo válido.")
        sys.exit(1)
    
    primos = obtener_primos(limite)
    print(f"Números primos entre 1 y {limite} son:\n")
    for p in primos:
        print(p)

if __name__ == "__main__":
    main()

"""
Se logra con esta version:

Código modular y reutilizable.

Entrada por parámetro para mayor flexibilidad.

Compatible con cualquier versión moderna de Python.

Portabilidad entre sistemas operativos.

Fácil de importar en otros programas.
"""