import unittest
import sys
import os

# --- INICIO DEL AJUSTE DE RUTA ---
# Esto permite que Python encuentre el archivo calculadora.py en la carpeta '../src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
# --- FIN DEL AJUSTE DE RUTA ---

# Ahora sí podemos importar normalmente
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
        # Verificamos que lance error al dividir por 0
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()