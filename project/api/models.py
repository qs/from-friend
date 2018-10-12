from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ff_category'


class Subscription(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ff_subscription'
