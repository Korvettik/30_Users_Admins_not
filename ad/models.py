from django.db import models
from django.db.models import CASCADE

from category.models import Category
from user.models import User


class Ad(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	author = models.ForeignKey(User, on_delete=CASCADE)
	price = models.IntegerField()
	description = models.TextField(max_length=1000)
	is_published = models.BooleanField()
	image = models.ImageField(upload_to='images/')
	category = models.ForeignKey(Category, on_delete=CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'Объявление'
		verbose_name_plural = 'Объявления'

	def __str__(self):
		return self.name


class Selection(models.Model):
	name = models.CharField(max_length=50)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	items = models.ManyToManyField(Ad)

	class Meta:
		verbose_name = 'Подборка'
		verbose_name_plural = 'Подборки'

	def __str__(self):
		return self.name
