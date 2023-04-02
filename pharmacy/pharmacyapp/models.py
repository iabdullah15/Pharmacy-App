from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=150)
    categoryID = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="categoryID")
    price = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    message = models.TextField(default="")