from rest_framework import serializers
from user.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	location = serializers.SlugRelatedField(
		read_only=True,
		slug_field='name'
	)

	class Meta:
		model = User
		exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	location = serializers.SlugRelatedField(
		required=False,
		slug_field='name',
		queryset=Location.objects.all(),
	)

	class Meta:
		model = User
		fields = '__all__'

	def is_valid(self, raise_exception=False):
		self._location = self.initial_data.pop('location', None)
		return super().is_valid(raise_exception=raise_exception)

	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(user.password)
		if self._location:
			location_obj = Location.objects.get_or_create(name=self._location)[0]
			user.location = location_obj
		user.save()
		return user


class UserUpdateSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	location = serializers.SlugRelatedField(
		required=False,
		slug_field='name',
		queryset=Location.objects.all(),
	)

	class Meta:
		model = User
		fields = '__all__'

	def is_valid(self, raise_exception=False):
		self._location = self.initial_data.pop('location', None)
		return super().is_valid(raise_exception=raise_exception)

	def save(self):
		user = super().save()
		user.set_password(user.password)
		if self._location:
			location_obj = Location.objects.get_or_create(name=self._location)[0]
			user.location = location_obj
		user.save()
		return user


class UserDestroySerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id']
