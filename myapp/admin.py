from django.contrib import admin
from myapp.models import Forms
# Register your models here.

class FormsAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Forms,FormsAdmin)