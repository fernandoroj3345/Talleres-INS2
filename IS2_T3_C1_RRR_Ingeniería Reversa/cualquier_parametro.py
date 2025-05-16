import sys

def es_primo(num):
    """Determina si un número es primo."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def obtener_primos(hasta):
    """Devuelve una lista de números primos entre 1 y 'hasta' (inclusive)."""
    return [n for n in range(1, hasta + 1) if es_primo(n)]

def main():
    if len(sys.argv) != 2:
        print("Uso: python new_primes.py <número_límite>")
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

if __name__ == "__main__":
    main()

"""
Desde otro script de Python:
Se puedes importar y usar la función obtener_primos() directamente:

#from new_primes import obtener_primos

#print(obtener_primos(20))


"""