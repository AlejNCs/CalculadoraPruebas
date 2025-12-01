# 🧪 Documentación de pruebas - Calculadora

## 1. Prueba Unitaria
**Nombre:** test_sumar  
**Archivo:** `test_calculadora.py`  
**Descripción:**  
Verifica que la función `sumar(a, b)` retorne el resultado correcto para diferentes casos:
- Suma de dos números positivos.
- Suma de un número negativo y uno positivo.
- Suma de ceros.

**Resultado esperado:**  
La función debe devolver la suma correcta en todos los casos.

---

## 2. Prueba de Integración
**Nombre:** test_operaciones_encadenadas  
**Archivo:** `test_calculadora.py`  
**Descripción:**  
Evalúa que las funciones puedan trabajar en conjunto correctamente.  
Ejemplo de flujo integrado:
1. Se suma `3 + 2` → resultado = 5  
2. Se multiplica por `4` → resultado = 20  
3. Se resta `5` → resultado final = 15

**Resultado esperado:**  
El resultado final debe ser `15`, demostrando que las funciones se integran correctamente.

---

## 3. Prueba de Rendimiento (Propuesta)
**Nombre:** test_rendimiento_sumas_masivas  
**Archivo:** *no implementada (propuesta)*  
**Descripción:**  
Simula un caso en el que la función `sumar()` se ejecuta miles de veces seguidas (por ejemplo, 100,000 sumas).  
Se mediría el tiempo de ejecución para evaluar el rendimiento y posibles cuellos de botella.

**Pseudocódigo:**
```python
import time
inicio = time.time()
for i in range(100000):
    sumar(i, i+1)
fin = time.time()
print("Tiempo total:", fin - inicio)
