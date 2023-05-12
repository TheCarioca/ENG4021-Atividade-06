from django.contrib import admin

# Register your models here.
from .models import Task, University, Category, Language, Hability

admin.site.register(Task)
admin.site.register(University)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Hability)