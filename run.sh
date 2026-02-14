#!/bin/bash
# Script de execução para Linux e macOS
# Garante que o ambiente virtual seja criado e as dependências instaladas.

PROJECT_NAME="batalhaNaval.py"
VENV_PATH="venv"
REQUIREMENTS="requirements.txt"

# --- 1. VERIFICA E CRIA O AMBIENTE VIRTUAL ---
if [ ! -d "$VENV_PATH" ]; then
    echo "Ambiente virtual '$VENV_PATH' não encontrado. Criando..."
    
    # Tenta usar python3, depois python, que são nomes comuns para o interpretador.
    if command -v python3 &> /dev/null
    then
        python3 -m venv "$VENV_PATH"
    elif command -v python &> /dev/null
    then
        python -m venv "$VENV_PATH"
    else
        echo "ERRO: Nenhum interpretador Python (python3 ou python) encontrado no sistema."
        exit 1
    fi
fi

# --- 2. INSTALA DEPENDÊNCIAS USANDO O PIP DO VENV ---

# Garante permissão de execução para o pip do venv (útil após descompactação)
chmod +x ./"$VENV_PATH"/bin/pip

echo "Instalando dependências listadas em $REQUIREMENTS..."
# Usa o PIP DENTRO do venv para instalar os pacotes
./"$VENV_PATH"/bin/pip install -r "$REQUIREMENTS"

# Verifica se a instalação foi bem-sucedida
if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao instalar as dependências. Verifique sua conexão e o arquivo $REQUIREMENTS."
    exit 1
fi

# --- 3. EXECUTA O JOGO ---
echo "Executando o jogo $PROJECT_NAME..."

# Garante permissão de execução para o interpretador Python do venv
chmod +x ./"$VENV_PATH"/bin/python

# Executa o script Python usando o interpretador do VENV
./"$VENV_PATH"/bin/python "$PROJECT_NAME"