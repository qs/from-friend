from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Subscription(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
