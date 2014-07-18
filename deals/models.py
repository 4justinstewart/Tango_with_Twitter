from django.db import models

# Create your models here.

class Company(models.Model):
    address = models.CharField(max_length=255)
    twitter_handle = models.CharField(max_length=15) #Twitter user-names are limited to 15 characters

    def __unicode__(self):
        return self.address


class Deal(models.Model):
    company = models.ForeignKey(Company)
    body = models.CharField(max_length=140)

    def __unicode__(self):
        return self.body



