from django.db import models

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    description = models.TextField()
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    mail = models.EmailField(max_length=200, null=True, blank=True)