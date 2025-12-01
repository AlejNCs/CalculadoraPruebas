# test_calculadora.py
import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    # Prueba unitaria: validar suma correcta
    def test_sumar(self):
        self.assertEqual(sumar(3, 5), 8)
        self.assertEqual(sumar(-2, 2), 0)
        self.assertEqual(sumar(0, 0), 0)

    # Prueba de integración: operaciones encadenadas
    def test_operaciones_encadenadas(self):
        # Ejemplo: (3 + 2) * 4 - 5 = 15
        resultado = restar(multiplicar(sumar(3, 2), 4), 5)
        self.assertEqual(resultado, 15)

    # Prueba de división (extra)
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == "__main__":
    unittest.main()
