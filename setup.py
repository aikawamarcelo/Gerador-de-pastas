import sys
import os
from cx_Freeze import setup, Executable

# Configurações para a criação do executável
build_exe_options = {
    "packages": ["os"], # Adicione outros pacotes que seu script usa
    "excludes": ["tkinter"], # Exclua pacotes que não são necessários
    "include_files": [] # Adicione outros arquivos que o script precisa (ex: arquivos de dados, imagens)
}

# Base para garantir que a janela do console não apareça em aplicações GUI (opcional)
base = "Win32GUI" if os.name == "nt" else None # "nt" significa Windows
  # Use Win32GUI para evitar a janela do console

executables = [Executable("Gera_Pastas.pyw", base=base)] # Use .pyw

setup(
    name="GeradorDePastas",
    version="1.0",
    description="Descrição do seu aplicativo",
    executables=executables
)