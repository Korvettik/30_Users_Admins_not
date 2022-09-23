from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class Location(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

	class Meta:
		verbose_name = 'Локация'
		verbose_name_plural = 'Локации'

	def __str__(self):
		return self.name


class User(AbstractUser):
	MEMBER = 'member'
	MODERATOR = 'moderator'
	ADMIN = 'admin'
	ROLES = [
		(MEMBER, 'Пользователь'),
		(MODERATOR, 'Модератор'),
		(ADMIN, 'Администратор'),
	]

	role = models.CharField(max_length=9, choices=ROLES)
	age = models.PositiveIntegerField(null=True, blank=True)
	location = models.ForeignKey(Location, on_delete=CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

	def __str__(self):
		return self.username
