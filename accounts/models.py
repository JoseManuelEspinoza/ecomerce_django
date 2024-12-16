from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('superuser', 'Superusuario'),
        ('store_admin', 'Administrador de Tienda'),
        ('customer', 'Cliente')
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, null=True, blank=True)