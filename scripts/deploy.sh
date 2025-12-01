#!/bin/bash
# 1. Detener el contenedor anterior si existe (para actualizar)
docker rm -f calculadora-app || true

# 2. Arrancar el nuevo contenedor en el puerto 5000
# -d: en segundo plano (detach)
# -p: conecta el puerto 5000 de tu PC con el 5000 del contenedor
docker run -d -p 5000:5000 --name calculadora-app mi-calculadora:latest

echo "Despliegue exitoso. La calculadora corre en http://localhost:5000"