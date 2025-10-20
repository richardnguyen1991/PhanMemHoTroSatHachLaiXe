"""
WSGI config for phan_mem_ho_tro_sat_hach_lai_xe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "phan_mem_ho_tro_sat_hach_lai_xe.settings"
)

application = get_wsgi_application()
