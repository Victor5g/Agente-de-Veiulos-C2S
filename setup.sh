#!/bin/bash

VENV_DIR="venv"

if ! command -v python3 &> /dev/null; then
    echo "❌ Erro: Python 3 não encontrado. Instale o Python 3.10.10 ou superior."
    exit 1
fi

echo "Verificando virtualenv...⚙️"
rm -rf "$VENV_DIR"

echo "Atualizando virtualenv...🔄"
python3 -m venv "$VENV_DIR"

echo "Ativando virtualenv...✅"
source "$VENV_DIR/bin/activate"

echo "Instalando dependências...⬇️"
pip install -r requirements.txt

OS_TYPE="$(uname)"

if [[ "$OS_TYPE" == "Linux" ]]; then
    echo "Detectado Linux 🐧"
    gnome-terminal -- bash -c "source $VENV_DIR/bin/activate && python main_server.py; exec bash"
    gnome-terminal -- bash -c "source $VENV_DIR/bin/activate && python main_client.py; exec bash"

elif [[ "$OS_TYPE" == "Darwin" ]]; then
    echo "Detectado macOS 🍎"
    osascript <<EOF
tell application "Terminal"
    do script "cd \"$(pwd)\"; source $VENV_DIR/bin/activate; python main_server.py"
    delay 1
    do script "cd \"$(pwd)\"; source $VENV_DIR/bin/activate; python main_client.py"
end tell
EOF

else
    echo "❌ Sistema operacional não suportado/Configurado para abrir os terminais automaticamente: $OS_TYPE"
    echo "Execute manualmente na raiz do projeto"
    echo "python3 main_server.py (Iniciar Servidor)"
    echo "python3 main_client.py (Iniciar Cliente)"
    exit 1
fi
