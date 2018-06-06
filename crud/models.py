from django.db import models


class Produto(models.Model):
	nome = models.CharField(max_length=100)
	marca = models.CharField(max_length=100)
	quantidade = models.IntegerField()

	def __str__(self):
		return self.nome
# Create your models here.
