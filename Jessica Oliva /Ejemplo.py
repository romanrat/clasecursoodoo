def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}.")
