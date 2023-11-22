from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)    
    photo = models.ImageField(upload_to='static/images', blank=True, null=True)


class Users(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
   

    def __str__(self):
        return f'{self.id}'



    

