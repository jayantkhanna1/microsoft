from django.contrib import admin
from .models import Feedback, Admin, Training

# Register your models here.

admin.site.register(Feedback)
admin.site.register(Admin)
admin.site.register(Training)