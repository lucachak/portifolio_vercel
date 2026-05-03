#!/bin/bash
echo "BUILD START"

# Adicionamos a flag --break-system-packages para ignorar o bloqueio do Python 3.12
python3 -m pip install -r requirements.txt --break-system-packages

# Coleta os arquivos estáticos (CSS, JS, Imagens)
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"