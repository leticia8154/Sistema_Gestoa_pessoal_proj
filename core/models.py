from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"Receita: {self.descricao} - R$ {self.valor}"


class Despesa(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"Despesa: {self.descricao} - R$ {self.valor}"