from django.contrib import admin
from .models import Admin, Training, Blogs, Chapter

# Register your models here.

admin.site.register(Admin)
admin.site.register(Training)
admin.site.register(Blogs)
admin.site.register(Chapter)