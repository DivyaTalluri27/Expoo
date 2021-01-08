from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    startDate=models.DateField(null=True)
    endDate=models.DateField(null=True)
    status=models.TextField(max_length=3)
    registrationCharge=models.IntegerField()
    registrationTax=models.IntegerField()
    registrationTotal=models.IntegerField()
    fileUpload=models.URLField()
    description=models.TextField(max_length=3000)

class Supportedby(models.Model):
    nameofthecompany=models.CharField(max_length=100)
    imgurl=models.ImageField()
    Event=models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)

class our_partner(models.Model):
    name=models.CharField(max_length=200)
    img_url=models.URLField(max_length=500)
    link=models.URLField(max_length=500)
    event=models.ForeignKey(Event, default=1, on_delete=models.SET_NULL, null=True)

class Association(models.Model):
    name=models.CharField(max_length=200)
    img_url=models.URLField(max_length=500)
    link=models.URLField(max_length=500)
    event=models.ForeignKey(Event, default=1, on_delete=models.SET_NULL, null=True)

class Media_Partner(models.Model):
    name=models.CharField(max_length=200)
    img_url=models.URLField(max_length=500)
    link=models.URLField(max_length=500)
    event=models.ForeignKey(Event, default=1, on_delete=models.SET_NULL, null=True)

class Testimonials(models.Model):
    byname=models.CharField(max_length=200)
    img_url=models.URLField(max_length=500)
    vidio_url=models.URLField(max_length=500)
    comment=models.TextField(max_length=4000)
    event=models.ForeignKey(Event, default=1, on_delete=models.SET_NULL, null=True)

class Speakers(models.Model):
    name=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    img_url=models.URLField(max_length=500)
    fb_link=models.URLField(max_length=500)
    twitter_link=models.URLField(max_length=500)
    description=models.TextField(max_length=4000)
    event=models.ForeignKey(Event, default=1, on_delete=models.SET_NULL, null=True)








