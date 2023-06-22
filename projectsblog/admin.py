from django.contrib import admin
from .models import Projects,Tag
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title','created']
    list_filter=('created',)

admin.site.register(Projects,ProjectsAdmin)
admin.site.register(Tag)
