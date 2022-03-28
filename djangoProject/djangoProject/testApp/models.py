from django.db import models
from django.urls import reverse

class Comida(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()

