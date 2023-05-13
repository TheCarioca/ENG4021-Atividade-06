from django.contrib import admin

# Importando cada modelo necessário para o admin.
from .models import Task, University, Category, Language, Hability

# Registrando cada modelo no admin para que possamos editar no /admin.
admin.site.register(Task)
admin.site.register(University)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Hability)