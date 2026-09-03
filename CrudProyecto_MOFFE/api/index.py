import os
import sys

# Agrega la carpeta contenedora (CrudProyecto_MOFFE) al path
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')

app = get_wsgi_application()