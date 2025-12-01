from prometheus_client import Counter, Histogram, start_http_server
import time

# Métricas
OPERATIONS_TOTAL = Counter(
    'calculator_operations_total',
    'Total de operaciones realizadas',
    ['operation']
)

ERRORS_TOTAL = Counter(
    'calculator_errors_total',
    'Total de errores en operaciones',
    ['operation']
)

LATENCY = Histogram(
    'calculator_operation_latency_seconds',
    'Tiempo de ejecución de cada operación',
    ['operation']
)

def suma(a, b):
    op = 'suma'
    start = time.time()
    try:
        result = a + b
        OPERATIONS_TOTAL.labels(operation=op).inc()
        LATENCY.labels(operation=op).observe(time.time() - start)
        return result
    except Exception:
        ERRORS_TOTAL.labels(operation=op).inc()
        raise

def resta(a, b):
    op = 'resta'
    start = time.time()
    try:
        result = a - b
        OPERATIONS_TOTAL.labels(operation=op).inc()
        LATENCY.labels(operation=op).observe(time.time() - start)
        return result
    except Exception:
        ERRORS_TOTAL.labels(operation=op).inc()
        raise

def multiplicacion(a, b):
    op = 'multiplicacion'
    start = time.time()
    try:
        result = a * b
        OPERATIONS_TOTAL.labels(operation=op).inc()
        LATENCY.labels(operation=op).observe(time.time() - start)
        return result
    except Exception:
        ERRORS_TOTAL.labels(operation=op).inc()
        raise

def division(a, b):
    op = 'division'
    start = time.time()
    try:
        result = a / b
        OPERATIONS_TOTAL.labels(operation=op).inc()
        LATENCY.labels(operation=op).observe(time.time() - start)
        return result
    except ZeroDivisionError:
        ERRORS_TOTAL.labels(operation=op).inc()
        print("Error: división entre cero")
        return None
    except Exception:
        ERRORS_TOTAL.labels(operation=op).inc()
        raise

def menu():
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '5':
            break

        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print("Resultado:", suma(a, b))
        elif opcion == '2':
            print("Resultado:", resta(a, b))
        elif opcion == '3':
            print("Resultado:", multiplicacion(a, b))
        elif opcion == '4':
            print("Resultado:", division(a, b))
        else:
            print("Opción no válida")

if __name__ == "__main__":
    # Levanta el servidor de métricas de Prometheus en el puerto 8000
    start_http_server(8000)
    print("Servidor de métricas expuesto en http://localhost:8000/metrics")

    # Corre la calculadora
    menu()
