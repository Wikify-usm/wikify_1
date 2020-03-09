from django.db import models

class Persona(models.Model):
    Apellidos:models.CharField(max_length=20)
    Nombres: models.CharField(max_length=20)
    nombredeusario:models.CharField(max_length=20)
    edad: models.IntegerField()
    Sexo:models.CharField(choices=[('F', 'femenino'), ('M', 'masculino')], default='M', max_length=1)
    email:models.EmailField(max_length=254)
