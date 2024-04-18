import uuid
from django.db import models

class User(models.Model):
	email = models.EmailField(primary_key=True)

	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'email'
	is_anonymous = False
	is_authenticated = False

class Token(models.Model):
	email = models.EmailField()
	uid = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4)