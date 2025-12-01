# test_integracion_calculadora.py
from calculadora import sumar, restar, multiplicar, dividir

def test_operaciones_encadenadas():
    """
    Flujo integrado:
    (((5 + 3) * 2) - 4) / 2  = 4.0
    """
    # Arrange
    a, b, c, d, e = 5, 3, 2, 4, 2

    # Act (encadenado)
    r1 = sumar(a, b)             # 5 + 3 = 8
    r2 = multiplicar(r1, c)      # 8 * 2 = 16
    r3 = restar(r2, d)           # 16 - 4 = 12
    r4 = dividir(r3, e)          # 12 / 2 = 6

    # Assert
    assert r4 == 6

def test_encadenado_con_decimales():
    """
    Flujo:
    ((10 / 4) + 1.5) * 3 - 2  =  (2.5 + 1.5)*3 - 2 = 4*3 - 2 = 12 - 2 = 10
    """
    r1 = dividir(10, 4)          # 2.5
    r2 = sumar(r1, 1.5)          # 4.0
    r3 = multiplicar(r2, 3)      # 12.0
    r4 = restar(r3, 2)           # 10.0
    assert r4 == 10.0

def test_encadenado_con_manejo_de_error():
    """
    Verifica que al intentar dividir entre 0 en una cadena,
    se lance ValueError (como tu menú maneja).
    """
    r1 = sumar(1, 1)             # 2
    try:
        _ = dividir(r1, 0)
        assert False, "Se esperaba ValueError por división entre cero"
    except ValueError:
        assert True
