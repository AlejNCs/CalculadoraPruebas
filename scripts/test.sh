#!/bin/bash
# Ejecutar los tests usando el módulo unittest de Python
# La variable PYTHONPATH asegura que encuentre tu código en src/
export PYTHONPATH=src
python -m unittest discover -s tests -p "test_*.py"