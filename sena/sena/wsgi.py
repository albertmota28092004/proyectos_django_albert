"""
WSGI config for sena project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# assuming your Django settings file is at '/home/mascotitas/sena/sena/settings.py'

path = '/home/mascotitas/sena'
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sena.settings')

application = get_wsgi_application()
