from django.contrib import admin
from .models import Feedback, Admin

# Register your models here.

admin.site.register(Feedback)
admin.site.register(Admin)