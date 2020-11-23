from django.contrib import admin
from hello.models import Entry,BMI

# Register your models here.

admin.site.register(Entry)   #allow you to see the model on the admin dashboard
admin.site.register(BMI) 