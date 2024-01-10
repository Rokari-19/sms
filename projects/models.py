from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Classname(models.Model):
    name = models.CharField(max_length=255)
    Lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Workname(models.Model):
    name = models.CharField(max_length=255)
    classname = models.ForeignKey(Classname, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_on = models.DateTimeField(blank=True, null=True)
    mark_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    