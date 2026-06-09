import os
import sys

from django.core.wsgi import get_wsgi_application

# Isso garante que o Python encontre a pasta mãe do projeto caso ocorra erro de escopo
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

application = get_wsgi_application()