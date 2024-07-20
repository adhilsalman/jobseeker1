from django.contrib import admin

# Register your models here.
from app.models import job,Category,student
admin.site.register(Category)
admin.site.register(job)
admin.site.register(student)