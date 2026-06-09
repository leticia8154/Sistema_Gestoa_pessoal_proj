#!/usr/bin/env python
"""Script de utilidade para tarefas administrativas do Django."""
import os
import sys

def main():
    """Executa as tarefas administrativas do projeto."""
    # Aponta explicitamente para as configurações da sua pasta setup
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Tem a certeza de que está instalado e "
            "disponível na variável de ambiente PYTHONPATH? Esqueceu-se de "
            "ativar o ambiente virtual (venv)?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()