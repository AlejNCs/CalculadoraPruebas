from flask import Flask, request, jsonify
from calculadora import sumar, restar, multiplicar, dividir

# Prometheus
from prometheus_client import Counter, Histogram, start_http_server
import time

app = Flask(__name__)

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


@app.route('/')
def home():
    return "Calculadora API v1.0 funcionando"


@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json() or {}
    op = data.get('operacion')
    a = data.get('a')
    b = data.get('b')

    if op is None or a is None or b is None:
        return jsonify({"error": "Faltan parámetros (operacion, a, b)"}), 400

    start_time = time.time()

    try:
        if op == 'sumar':
            res = sumar(a, b)
        elif op == 'restar':
            res = restar(a, b)
        elif op == 'multiplicar':
            res = multiplicar(a, b)
        elif op == 'dividir':
            res = dividir(a, b)
        else:
            return jsonify({"error": "Operacion no valida"}), 400

        # Métricas OK
        OPERATIONS_TOTAL.labels(operation=op).inc()
        LATENCY.labels(operation=op).observe(time.time() - start_time)

        return jsonify({"resultado": res})

    except ValueError as e:
        # Errores esperados (por ejemplo división entre cero)
        ERRORS_TOTAL.labels(operation=op or "desconocida").inc()
        return jsonify({"error": str(e)}), 400
    except Exception:
        ERRORS_TOTAL.labels(operation=op or "desconocida").inc()
        return jsonify({"error": "Error interno"}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "up"}), 200


if __name__ == '__main__':
    # servidor de métricas en 8000
    start_http_server(8000)
    print("Servidor de métricas en http://localhost:8000/metrics")

    # API Flask en 5000
    app.run(host='0.0.0.0', port=5000)
