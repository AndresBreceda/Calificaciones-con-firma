from django.db import models

# Create your models here.
class Registro(models.Model):
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto