from django.db import models


class post(models.Model):
    text = models.TextField(verbose_name='Text')

    def __str__(self):
        return self.text[:50]


class MyModel(models.Model):
    customer_id = models.CharField(max_length=12, primary_key=True, verbose_name='Customer Id')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:20]
    

class MyModel1(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:20]
    

class Product(models.Model):
    date_created = models.CharField(max_length=20)


class Product1(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    add_to_cart = models.BooleanField(default=False)
    email = models.EmailField()
    available_quantity = models.PositiveIntegerField()
    



