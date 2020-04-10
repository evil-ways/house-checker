from django.db import models

class Imovirtual(models.Model):
    Titulo = models.TextField()
    Preco = models.TextField()
    PrecoArea = models.TextField()
    Localizacao = models.TextField()
    Propriedades = models.TextField()
    Caracteristicas = models.TextField()
    Imobiliaria = models.TextField()
    Descricao = models.TextField()
    Tipo = models.TextField()

