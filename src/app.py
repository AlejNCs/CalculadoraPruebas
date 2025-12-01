from flask import Flask, request, jsonify
# Importamos tu clase o funciones existentes
from calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)

@app.route('/')
def home():
    return "Calculadora API v1.0 funcionando"

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    op = data.get('operacion')
    a = data.get('a')
    b = data.get('b')

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
        
        return jsonify({"resultado": res})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno"}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "up"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)