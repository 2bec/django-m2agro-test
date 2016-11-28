from __future__ import unicode_literals

from django.db import models


class NoDeleteQuerySet(models.query.QuerySet):

	def delete(self):
		self.update(is_active=False)

class Produto(models.Model):

	nome = models.CharField(max_length=180, blank=False, null=False)
	preco_medio = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	objects = NoDeleteQuerySet()

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.nome

	def delete(self):
		self.is_active = False
		self.save()