from django.db import models


# Create your models here.

class Contact(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    company = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactNumber(models.Model):
    NUMBER_TYPES = (('home', 'home'), ('work', 'work'), ('mobile', 'mobile'),)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE,related_name='contactnumbers')
    number = models.CharField(max_length=20)
    type = models.CharField(choices=NUMBER_TYPES,max_length=10)

    def __str__(self):
        return f"{self.contact} ({self.type}): {self.number}"
