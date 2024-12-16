# stores/models.py

from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

class Store(TenantMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    category = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    # Agregar cualquier otro campo relevante

    auto_create_schema = True  # Crear esquema automáticamente al guardar

class Domain(DomainMixin):
    pass
