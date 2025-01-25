def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def isNumber(valor):
    """Indica si el argumento introducido es un número o no."""
    try:
        float(valor)  # Intentar convertir a número
        return True
    except ValueError:
        return False

def mayorCero(numero):
    """Indica si el número pasado es mayor que cero."""
    if not isNumber(numero):
        return "Error: El valor no es un número."
    return float(numero) > 0

def calculadora():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    operacion = input("Ingrese el número de la operación (1/2/3/4): ")
    
    if operacion in ['1', '2', '3', '4']:
        num1 = input("Ingrese el primer número: ")
        num2 = input("Ingrese el segundo número: ")

        # Validar que ambos números sean válidos
        if not isNumber(num1) or not isNumber(num2):
            print("Error: Ambos valores deben ser números válidos.")
            return

        # Convertir a float después de validar
        num1 = float(num1)
        num2 = float(num2)

        # Realizar la operación seleccionada
        if operacion == '1':
            print("Resultado:", suma(num1, num2))
        elif operacion == '2':
            print("Resultado:", resta(num1, num2))
        elif operacion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif operacion == '4':
            print("Resultado:", division(num1, num2))
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    calculadora()


