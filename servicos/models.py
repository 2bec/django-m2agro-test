from __future__ import unicode_literals

from django.db import models

from safras.models import Safra
from produtos.models import Produto


class Servico(models.Model):
	nome = models.CharField(max_length=180, blank=False, null=False)
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	safra = models.ForeignKey(Safra)
	produtos = models.ManyToManyField(Produto, through="Valores")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ('data_inicio',)

	def __str__(self):
		return self.nome

	def delete(self):
		self.is_active = False
		self.save()

	def get_custo_total(self):
		"""
		Calcula o custo total de um servico
		"""
		total = 0
		for v in self.valores_set.all():
			total += v.preco
		return total


class Valores(models.Model):
	produto = models.ForeignKey(Produto)
	servico = models.ForeignKey(Servico)
	preco = models.DecimalField(max_digits=5,decimal_places=2)
	quantidade = models.DecimalField(max_digits=5, decimal_places=2)
	data_compra = models.DateTimeField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ('servico',)

	def __str__(self):
		return self.produto.nome

	def delete(self):
		self.is_active = False
		self.save()