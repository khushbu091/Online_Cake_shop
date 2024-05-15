from django.db import models

# Create your models here.
class User(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.IntegerField()

    class Meta:
        db_table='User'
    def __str__(self):
        return self.Firstname