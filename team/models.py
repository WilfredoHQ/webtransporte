from django.db import models

def custom_upload_to(instance, filename):
    try:
        old_instance = Employee.objects.get(pk=instance.pk)
        old_instance.avatar.delete()
    finally:
        return 'employees/' + filename

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    description = models.TextField()
    avatar = models.ImageField(upload_to=custom_upload_to)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    mail = models.EmailField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name