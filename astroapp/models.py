from django.db import models

class contact_form(models.Model):
    name = models.CharField(max_length=15,null=True)
    lastname = models.CharField(max_length=15,null=True)
    subject = models.CharField(max_length=15,null=True)
    email = models.EmailField(max_length=50,null=True)
    message = models.CharField(max_length=150,null=True)