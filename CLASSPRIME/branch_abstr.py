import sys

class ClassPrimes:
    def compute(self, num): #Se introduce una nueva rama de ejecución (validador.compute(num)) 
                            #que usa la clase ClassPrimes si se proporciona.
                            #Si no se proporciona un objeto, se usa la implementación original,
                            #manteniendo intacto el comportamiento del programa.
                            #Esta función actúa como una capa de abstracción que une el código 
                            #estructurado con la nueva versión orientada a objetos
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

    
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

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

    validador = ClassPrimes()  # Aplicando POO
    primos = obtener_primos(limite, validador)
    
    print(f"Números primos entre 1 y {limite} son:\n")
    for p in primos:
        print(p)

if __name__ == "__main__":
    main()
