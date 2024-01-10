from django.contrib import admin

from .models import Category, Workname, Classname
# Register your models here.

admin.site.register(Category)
admin.site.register(Workname)
admin.site.register(Classname)