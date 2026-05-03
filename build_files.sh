#!/bin/bash
echo "BUILD START"

# Instala as dependências usando a versão correta do Python
python3 -m pip install -r requirements.txt

# Coleta os arquivos estáticos (CSS, JS, Imagens)
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"