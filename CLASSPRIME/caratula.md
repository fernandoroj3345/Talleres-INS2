# ------------------------------------------------------------------------------
# Nombre del archivo: branch_abstr.py
# Descripción: Programa que imprime números primos hasta un valor dado usando
#              una implementación orientada a objetos con estrategia de
#              Branching by Abstraction.
#
# Autor: Fernando Martin Rojas
# Versión: 1.1
# Fecha de última modificación: 2024-05-24
#
# Copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados.
# ------------------------------------------------------------------------------

import sys

# Clase que encapsula la lógica para determinar si un número es primo
class ClassPrimes:
    def compute(self, num):
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

# Función intermedia que actúa como capa de abstracción (Branching by Abstraction)
def es_primo(num, validador=None):
    """
    Determina si un número es primo usando una clase si se proporciona.

    Parámetros:
        num (int): Número a verificar.
        validador (object): Objeto con método compute(num) que devuelve True/False.

    Retorna:
        bool: True si es primo, False en caso contrario.
    """
    if validador:
        return validador.compute(num)

    # Implementación tradicional como alternativa (fallback)
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Genera una lista de números primos entre 1 y el valor dado
def obtener_primos(hasta, validador=None):
    """
    Devuelve una lista de números primos entre 1 y 'hasta' (inclusive).
    
    Parámetros:
        hasta (int): Límite superior del rango.
        validador (object): Objeto con método compute(num) para verificar primos.
    
    Retorna:
        list: Lista de números primos.
    """
    return [n for n in range(1, hasta + 1) if es_primo(n, validador)]

# Función principal que gestiona la ejecución del programa desde la línea de comandos
def main():
    """
    Función principal que gestiona la entrada desde la línea de comandos.
    Valida el argumento de entrada y utiliza la clase ClassPrimes
    para calcular los números primos hasta ese valor.
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

    # Se crea una instancia de ClassPrimes para aplicar la lógica de primos
    validador = ClassPrimes()
    
    # Se obtiene la lista de números primos usando la clase
    primos = obtener_primos(limite, validador)
    
    # Se muestran los resultados
    print(f"Números primos entre 1 y {limite} son:\n")
    for p in primos:
        print(p)

# Punto de entrada del script
if __name__ == "__main__":
    main()
