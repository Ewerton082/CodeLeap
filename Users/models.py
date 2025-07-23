from django.db import models

# Create your models here.


class User(models.Model):

    user = models.CharField(max_length=60, null=False, blank=False,verbose_name="Nome de Usuário")

    def __str__(self):
        return f"{self.user}"
