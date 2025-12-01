# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos las dependencias e instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código (src, tests y scripts)
COPY src/ ./src/
COPY tests/ ./tests/
COPY scripts/ ./scripts/

# Le decimos a Python dónde buscar módulos
ENV PYTHONPATH=/app/src

# Exponemos el puerto 5000 para la API Web
EXPOSE 5000

# Comando para iniciar la app
CMD ["python", "src/app.py"]