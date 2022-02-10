from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    pass1=models.CharField(max_length=122)
    knlg=models.CharField(max_length=250)

    def __str__(self):
        return self.name