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
    status = models.BooleanField()

    def __str__(self):
        return f'{self.id}'


class Posts(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(default=None)
    text = models.TextField()
    likes = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.id}'
    
class Comments(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.id}'
    
