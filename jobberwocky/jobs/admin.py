from django.contrib import admin
from .models import JobUser, JobList

# Register your models here.
class JobUserAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la vista de lista
    list_display = ('first_name', 'last_name', 'email', 'position_wanted', 'salary_range_min', 'salary_range_max', 'created_at')
    
    # Filtros que se agregarán en el panel lateral
    list_filter = ('position_wanted', 'created_at')
    
    # Campos de búsqueda
    search_fields = ('first_name', 'last_name', 'email', 'position_wanted')


class JobAdmin(admin.ModelAdmin):
    # Mostrar ciertos campos en la vista de lista
    list_display = ('position', 'skill', 'city', 'country', 'work_type', 'salary_range_min', 'salary_range_max', 'created_at')
    
    # Filtros por tipo de trabajo
    list_filter = ('work_type', 'country', 'created_at')
    
    # Habilitar búsqueda por campos
    search_fields = ('position', 'country', 'city')

admin.site.register(JobList, JobAdmin)
admin.site.register(JobUser, JobUserAdmin)
