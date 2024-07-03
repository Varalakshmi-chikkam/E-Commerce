from django.db import models


class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=200)