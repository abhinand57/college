from django.db import models

# Create your models here.
class item(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class form(models.Model):
    fname=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    adress=models.TextField()
    email=models.EmailField()
    number=models.IntegerField()
    dob=models.IntegerField()
    age = models.IntegerField()

