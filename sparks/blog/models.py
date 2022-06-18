from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=100)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Publised_date = models.DateTimeField()

