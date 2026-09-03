import os
import sys

# Apunta al directorio padre (CrudProyecto_MOFFE)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')

app = get_wsgi_application()