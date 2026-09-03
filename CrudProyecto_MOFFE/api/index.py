import os
import sys

# Agrega la raíz del proyecto (CrudProyecto_MOFFE) al path de Python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# Define la ruta del módulo settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()