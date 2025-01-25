import unittest

# Código bajo prueba
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
    try:
        float(valor)
        return True
    except ValueError:
        return False

def mayorCero(numero):
    if not isNumber(numero):
        return "Error: El valor no es un número."
    return float(numero) > 0

# Pruebas unitarias
class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(5, 3), 8)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(-5, -3), -8)
        self.assertEqual(suma(1.5, 2.5), 4.0)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(-5, -3), -2)
        self.assertEqual(resta(5.5, 2.5), 3.0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 4), 12)
        self.assertEqual(multiplicacion(0, 5), 0)
        self.assertEqual(multiplicacion(-2, -3), 6)
        self.assertEqual(multiplicacion(2.5, 4), 10.0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5.0)
        self.assertEqual(division(5, 0), "Error: División por cero")
        self.assertEqual(division(0, 5), 0.0)
        self.assertEqual(division(-10, 2), -5.0)

    def test_isNumber(self):
        self.assertTrue(isNumber("123"))
        self.assertFalse(isNumber("abc"))
        self.assertTrue(isNumber("12.34"))
        self.assertFalse(isNumber(" "))

    def test_mayorCero(self):
        self.assertTrue(mayorCero("10"))
        self.assertFalse(mayorCero("-5"))
        self.assertEqual(mayorCero("abc"), "Error: El valor no es un número.")
        self.assertFalse(mayorCero("0"))

if __name__ == "__main__":
    unittest.main()