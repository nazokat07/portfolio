from django.db import models

class Product(models.Model):

    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-id']




class Users(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
   

    def __str__(self):
        return f'{self.id}'


class Posts(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    

    def __str__(self):
        return f'{self.id}'
    

