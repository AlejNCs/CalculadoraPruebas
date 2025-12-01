###Script para la generación del entorno de liberación

#!/bin/bash
# Construir la imagen Docker etiquetada como 'mi-calculadora'
#docker build -t mi-calculadora:latest .
#!/bin/bash
set -e

# Usar el Dockerfile que está en src/
docker build -t calculadora -f src/Dockerfile .