from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.CharField( max_length=150)
    desc = models.TextField()
    dateofpost=models.DateField()
    

    def __str__(self):
        return self.email
 