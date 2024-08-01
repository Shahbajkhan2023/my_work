from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    language = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True, unique=True)

    def __str__(self):
        return str(self.email)
    



class Author(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    




class Collections(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
    

class Book1(models.Model):
    collections = models.ManyToManyField(Collections)
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)
    
