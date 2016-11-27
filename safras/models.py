from __future__ import unicode_literals

from django.db import models


class Safra(models.Model):

	nome = models.CharField(max_length=180, blank=False, null=False)
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)

	class Meta:
		ordering = ('data_inicio',)

	def __str__(self):
		return self.nome