"""
ASGI config for phan_mem_ho_tro_sat_hach_lai_xe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "phan_mem_ho_tro_sat_hach_lai_xe.settings"
)

application = get_asgi_application()
