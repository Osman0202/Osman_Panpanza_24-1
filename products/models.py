from django.db import models

# Create your models here.


class Category(models.Model):
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50)


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField()
    price = models.FloatField(null=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.TextField()
    characteristics = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)