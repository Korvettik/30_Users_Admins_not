from django.db import models


class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['name']

	def __str__(self):
		return self.name
