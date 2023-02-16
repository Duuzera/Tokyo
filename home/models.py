from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    sobrenome = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=11)
    user = models.CharField(max_length=30)
    


    def __str__(self) -> str:
        return self.nome


